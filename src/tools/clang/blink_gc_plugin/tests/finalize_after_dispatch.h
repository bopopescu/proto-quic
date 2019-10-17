// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef FINALIZE_AFTER_DISPATCH_H_
#define FINALIZE_AFTER_DISPATCH_H_

#include "heap/stubs.h"

namespace blink {

class NeedsFinalize : public GarbageCollectedFinalized<NeedsFinalize> {
public:
    void Trace(Visitor*);
    void TraceAfterDispatch(Visitor*);
    // Needs a FinalizeGarbageCollectedObject method.
};

class NeedsDispatch : public GarbageCollectedFinalized<NeedsDispatch> {
public:
    void Trace(Visitor*);
    // Needs a TraceAfterDispatch method.
    void FinalizeGarbageCollectedObject() { };
};

class NeedsFinalizedBase : public GarbageCollected<NeedsFinalizedBase> {
public:
    void Trace(Visitor*) { };
    void TraceAfterDispatch(Visitor*) { };
    void FinalizeGarbageCollectedObject() { };
};

class A : GarbageCollectedFinalized<A> {
public:
    void Trace(Visitor*);
    void TraceAfterDispatch(Visitor*);
    void FinalizeGarbageCollectedObject();
protected:
    enum Type { TB, TC, TD };
    A(Type type) : m_type(type) { }
private:
    Type m_type;
};

class B : public A {
public:
    B() : A(TB) { }
    ~B() { }
    void TraceAfterDispatch(Visitor*);
private:
    Member<A> m_a;
};

class C : public A {
public:
    C() : A(TC) { }
    void TraceAfterDispatch(Visitor*);
private:
    Member<A> m_a;
};

// This class is considered abstract does not need to be dispatched to.
class Abstract : public A {
protected:
    Abstract(Type type) : A(type) { }
};

class D : public Abstract {
public:
    D() : Abstract(TD) { }
    void TraceAfterDispatch(Visitor*);
private:
    Member<A> m_a;
};

}

#endif
