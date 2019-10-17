// Copyright 2016 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "stdafx.h"

#include <algorithm>

#include "system_information_sampler.h"

// From ntdef.h
typedef struct _UNICODE_STRING {
  USHORT Length;
  USHORT MaximumLength;
  PWCH Buffer;
} UNICODE_STRING;

// From <wdm.h>
typedef LONG KPRIORITY;
typedef LONG KWAIT_REASON;  // Full definition is in wdm.h

// From ntddk.h
typedef struct _VM_COUNTERS {
  SIZE_T PeakVirtualSize;
  SIZE_T VirtualSize;
  ULONG PageFaultCount;
  // Padding here in 64-bit
  SIZE_T PeakWorkingSetSize;
  SIZE_T WorkingSetSize;
  SIZE_T QuotaPeakPagedPoolUsage;
  SIZE_T QuotaPagedPoolUsage;
  SIZE_T QuotaPeakNonPagedPoolUsage;
  SIZE_T QuotaNonPagedPoolUsage;
  SIZE_T PagefileUsage;
  SIZE_T PeakPagefileUsage;
} VM_COUNTERS;

// Two possibilities available from here:
// http://stackoverflow.com/questions/28858849/where-is-system-information-class-defined

typedef enum _SYSTEM_INFORMATION_CLASS {
  SystemBasicInformation = 0,
  SystemPerformanceInformation = 2,
  SystemTimeOfDayInformation = 3,
  SystemProcessInformation = 5,  // This is the number that we need
  SystemProcessorPerformanceInformation = 8,
  SystemInterruptInformation = 23,
  SystemExceptionInformation = 33,
  SystemRegistryQuotaInformation = 37,
  SystemLookasideInformation = 45
} SYSTEM_INFORMATION_CLASS;

// https://msdn.microsoft.com/en-us/library/gg750647.aspx?f=255&MSPPError=-2147217396
typedef struct {
  HANDLE UniqueProcess;  // Actually process ID
  HANDLE UniqueThread;   // Actually thread ID
} CLIENT_ID;

// From http://alax.info/blog/1182, with corrections and modifications
// Originally from
// http://undocumented.ntinternals.net/index.html?page=UserMode%2FUndocumented%20Functions%2FSystem%20Information%2FStructures%2FSYSTEM_THREAD.html
struct SYSTEM_THREAD_INFORMATION {
  ULONGLONG KernelTime;
  ULONGLONG UserTime;
  ULONGLONG CreateTime;
  ULONG WaitTime;
  // Padding here in 64-bit
  PVOID StartAddress;
  CLIENT_ID ClientId;
  KPRIORITY Priority;
  LONG BasePriority;
  ULONG ContextSwitchCount;
  ULONG State;
  KWAIT_REASON WaitReason;
};
#if _M_X64
static_assert(sizeof(SYSTEM_THREAD_INFORMATION) == 80,
              "Structure size mismatch");
#else
static_assert(sizeof(SYSTEM_THREAD_INFORMATION) == 64,
              "Structure size mismatch");
#endif

// From http://alax.info/blog/1182, with corrections and modifications
// Originally from
// http://undocumented.ntinternals.net/index.html?page=UserMode%2FUndocumented%20Functions%2FSystem%20Information%2FStructures%2FSYSTEM_THREAD.html
struct SYSTEM_PROCESS_INFORMATION {
  ULONG NextEntryOffset;
  ULONG NumberOfThreads;
  // http://processhacker.sourceforge.net/doc/struct___s_y_s_t_e_m___p_r_o_c_e_s_s___i_n_f_o_r_m_a_t_i_o_n.html
  ULONGLONG WorkingSetPrivateSize;
  ULONG HardFaultCount;
  ULONG Reserved1;
  ULONGLONG CycleTime;
  ULONGLONG CreateTime;
  ULONGLONG UserTime;
  ULONGLONG KernelTime;
  UNICODE_STRING ImageName;
  KPRIORITY BasePriority;
  HANDLE ProcessId;
  HANDLE ParentProcessId;
  ULONG HandleCount;
  ULONG Reserved2[2];
  // Padding here in 64-bit
  VM_COUNTERS VirtualMemoryCounters;
  size_t Reserved3;
  IO_COUNTERS IoCounters;
  SYSTEM_THREAD_INFORMATION Threads[1];
};
#if _M_X64
static_assert(sizeof(SYSTEM_PROCESS_INFORMATION) == 336,
              "Structure size mismatch");
#else
static_assert(sizeof(SYSTEM_PROCESS_INFORMATION) == 248,
              "Structure size mismatch");
#endif

// ntstatus.h conflicts with windows.h so define this locally.
#define STATUS_SUCCESS ((NTSTATUS)0x00000000L)
#define STATUS_BUFFER_TOO_SMALL ((NTSTATUS)0xC0000023L)
#define STATUS_INFO_LENGTH_MISMATCH ((NTSTATUS)0xC0000004L)

typedef NTSTATUS(WINAPI* NTQUERYSYSTEMINFORMATION)(
    SYSTEM_INFORMATION_CLASS SystemInformationClass,
    PVOID SystemInformation,
    ULONG SystemInformationLength,
    PULONG ReturnLength);

__declspec(noreturn) void oops(const char* pMessage) {
  printf("%s\n", pMessage);
  exit(0);
}

// Simple memory buffer wrapper for passing the data out of
// QuerySystemProcessInformation.
class ByteBuffer {
 public:
  explicit ByteBuffer(size_t capacity) : size_(0), capacity_(0) {
    if (capacity > 0)
      grow(capacity);
  }

  ~ByteBuffer() {}

  BYTE* data() { return data_.get(); }

  size_t size() { return size_; }

  void set_size(size_t new_size) { size_ = new_size; }

  size_t capacity() { return capacity_; }

  void grow(size_t new_capacity) {
    capacity_ = new_capacity;
    data_.reset(new BYTE[new_capacity]);
  }

 private:
  std::unique_ptr<BYTE[]> data_;
  size_t size_;
  size_t capacity_;

  ByteBuffer& operator=(const ByteBuffer&) = delete;
  ByteBuffer(const ByteBuffer&) = delete;
};

// Wrapper for NtQuerySystemProcessInformation with buffer reallocation logic.
bool QuerySystemProcessInformation(ByteBuffer* buffer) {
  typedef NTSTATUS(WINAPI * NTQUERYSYSTEMINFORMATION)(
      SYSTEM_INFORMATION_CLASS SystemInformationClass, PVOID SystemInformation,
      ULONG SystemInformationLength, PULONG ReturnLength);

  HMODULE ntdll = GetModuleHandle(L"ntdll.dll");
  if (!ntdll) {
    oops("Couldn't load ntdll.dll");
  }

  NTQUERYSYSTEMINFORMATION nt_query_system_information_ptr =
      reinterpret_cast<NTQUERYSYSTEMINFORMATION>(
          GetProcAddress(ntdll, "NtQuerySystemInformation"));
  if (!nt_query_system_information_ptr)
    oops("Couldn't find NtQuerySystemInformation");

  NTSTATUS result;

  // There is a potential race condition between growing the buffer and new
  // processes being created. Try a few times before giving up.
  for (int i = 0; i < 10; i++) {
    ULONG data_size = 0;
    ULONG buffer_size = static_cast<ULONG>(buffer->capacity());
    result = nt_query_system_information_ptr(
        SystemProcessInformation, buffer->data(), buffer_size, &data_size);

    if (result == STATUS_SUCCESS) {
      buffer->set_size(data_size);
      break;
    }

    if (result == STATUS_INFO_LENGTH_MISMATCH ||
        result == STATUS_BUFFER_TOO_SMALL) {
      // Insufficient buffer. Grow to the returned |data_size| plus 10% extra
      // to avoid frequent reallocations and try again.
      buffer->grow(static_cast<ULONG>(data_size * 1.1));
    } else {
      // An error other than the two above.
      break;
    }
  }

  return result == STATUS_SUCCESS;
}

SystemInformationSampler::SystemInformationSampler(
    const wchar_t* process_name) {
  lstrcpyn(target_process_name_, process_name,
           sizeof(target_process_name_) / sizeof(wchar_t));

  QueryPerformanceFrequency(&perf_frequency_);
  QueryPerformanceCounter(&initial_counter_);
}

SystemInformationSampler::~SystemInformationSampler() {}

std::unique_ptr<ProcessDataSnapshot> SystemInformationSampler::TakeSnapshot() {
  // Preallocate the buffer with the size determined on the previous call to
  // QuerySystemProcessInformation. This should be sufficient most of the time.
  // QuerySystemProcessInformation will grow the buffer if necessary.
  ByteBuffer data_buffer(previous_buffer_size_);

  if (!QuerySystemProcessInformation(&data_buffer))
    return std::unique_ptr<ProcessDataSnapshot>();

  previous_buffer_size_ = data_buffer.capacity();

  std::unique_ptr<ProcessDataSnapshot> snapshot(new ProcessDataSnapshot);

  LARGE_INTEGER perf_counter_value;
  QueryPerformanceCounter(&perf_counter_value);
  snapshot->timestamp = static_cast<double>(
      (perf_counter_value.QuadPart - initial_counter_.QuadPart) /
      perf_frequency_.QuadPart);

  for (size_t offset = 0; offset < data_buffer.size();) {
    auto pi = reinterpret_cast<const SYSTEM_PROCESS_INFORMATION*>(
        data_buffer.data() + offset);

    // Validate that the offset is valid and all needed data is within
    // the buffer boundary.
    if (offset + sizeof(SYSTEM_PROCESS_INFORMATION) > data_buffer.size())
      break;
    if (offset + sizeof(SYSTEM_PROCESS_INFORMATION) +
            (pi->NumberOfThreads - 1) * sizeof(SYSTEM_THREAD_INFORMATION) >
        data_buffer.size())
      break;

    if (pi->ImageName.Buffer) {
      // Validate that the image name is within the buffer boundary.
      // ImageName.Length seems to be in bytes rather than characters.
      size_t image_name_offset =
          reinterpret_cast<BYTE*>(pi->ImageName.Buffer) - data_buffer.data();
      if (image_name_offset + pi->ImageName.Length > data_buffer.size())
        break;

      // Check if this is a chrome process. Ignore all other processes.
      if (wcsncmp(target_process_name_filter(), pi->ImageName.Buffer,
                  lstrlen(target_process_name_filter())) == 0) {
        // Collect enough data to be able to do a diff between two snapshots.
        // Some threads might stop or new threads might be created between two
        // snapshots. If a thread with a large number of context switches gets
        // terminated the total number of context switches for the process might
        // go down and the delta would be negative.
        // To avoid that we need to compare thread IDs between two snapshots and
        // not count context switches for threads that are missing in the most
        // recent snapshot.
        ProcessData process_data;

        process_data.cpu_time = pi->KernelTime + pi->UserTime;
        process_data.working_set = pi->WorkingSetPrivateSize;

        // Iterate over threads and store each thread's ID and number of context
        // switches.
        for (ULONG thread_index = 0; thread_index < pi->NumberOfThreads;
             ++thread_index) {
          const SYSTEM_THREAD_INFORMATION* ti = &pi->Threads[thread_index];
          if (ti->ClientId.UniqueProcess != pi->ProcessId)
            continue;

          ThreadData thread_data;
          thread_data.thread_id = ti->ClientId.UniqueThread;
          thread_data.context_switches = ti->ContextSwitchCount;
          process_data.threads.push_back(thread_data);
        }

        // Order thread data by thread ID to help diff two snapshots.
        std::sort(process_data.threads.begin(), process_data.threads.end(),
                  [](const ThreadData& l, const ThreadData r) {
                    return l.thread_id < r.thread_id;
                  });

        snapshot->processes.insert(
            std::make_pair(pi->ProcessId, std::move(process_data)));
      }
    }

    // Check for end of the list.
    if (!pi->NextEntryOffset)
      break;

    // Jump to the next entry.
    offset += pi->NextEntryOffset;
  }

  return snapshot;
}
