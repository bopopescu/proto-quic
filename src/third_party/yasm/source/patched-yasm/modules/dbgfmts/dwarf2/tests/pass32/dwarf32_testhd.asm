	.file	"test_hd.c"
	.section	.debug_abbrev,"",@progbits
.Ldebug_abbrev0:
	.section	.debug_info,"",@progbits
.Ldebug_info0:
	.section	.debug_line,"",@progbits
.Ldebug_line0:
	.text
.Ltext0:
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"Usage: %s <file>\n"
.LC1:
	.string	"rb"
.LC2:
	.string	"Could not open `%s'.\n"
.LC3:
	.string	"%02x \n"
.LC4:
	.string	"Error reading from `%s'.\n"
	.text
	.p2align 2,,3
.globl main
	.type	main, @function
main:
.LFB3:
	.file 1 "test_hd.c"
	.loc 1 33 0
	pushl	%ebp
.LCFI0:
	movl	%esp, %ebp
.LCFI1:
	pushl	%esi
.LCFI2:
	pushl	%ebx
.LCFI3:
	movl	12(%ebp), %esi
	andl	$-16, %esp
	subl	$16, %esp
	.loc 1 37 0
	cmpl	$2, 8(%ebp)
	je	.L2
	.loc 1 38 0
	subl	$4, %esp
	pushl	(%esi)
	pushl	$.LC0
	pushl	__stderrp
.LCFI4:
	call	fprintf
	.loc 1 39 0
	movl	$1, %eax
	jmp	.L1
	.p2align 2,,3
.L2:
	.loc 1 42 0
	subl	$8, %esp
	pushl	$.LC1
	pushl	4(%esi)
	call	fopen
	movl	%eax, %ebx
	.loc 1 44 0
	addl	$16, %esp
	testl	%eax, %eax
	jne	.L4
	.loc 1 45 0
	subl	$4, %esp
	pushl	4(%esi)
	pushl	$.LC2
	pushl	__stderrp
	call	fprintf
	.loc 1 46 0
	movl	$1, %eax
	jmp	.L1
	.p2align 2,,3
.L6:
	.loc 1 50 0
	subl	$8, %esp
	pushl	%eax
	pushl	$.LC3
	call	printf
	addl	$16, %esp
.L4:
	subl	$12, %esp
	pushl	%ebx
	call	fgetc
	addl	$16, %esp
	cmpl	$-1, %eax
	jne	.L6
	.loc 1 52 0
	cmpl	$0, __isthreaded
	jne	.L8
	testb	$64, 12(%ebx)
	jne	.L9
	jmp	.L7
.L8:
	subl	$12, %esp
	pushl	%ebx
	call	ferror
	addl	$16, %esp
	testl	%eax, %eax
	je	.L7
.L9:
	.loc 1 53 0
	subl	$4, %esp
	pushl	4(%esi)
	pushl	$.LC4
	pushl	__stderrp
	call	fprintf
	.loc 1 54 0
	movl	$1, %eax
	jmp	.L1
.L7:
	.loc 1 57 0
	subl	$12, %esp
	pushl	%ebx
	call	fclose
	.loc 1 58 0
	movl	$0, %eax
	.p2align 2,,3
.L1:
	.loc 1 59 0
	leal	-8(%ebp), %esp
	popl	%ebx
	popl	%esi
	leave
	ret
.LFE3:
	.size	main, .-main
	.section	.debug_frame,"",@progbits
.Lframe0:
	.long	.LECIE0-.LSCIE0
.LSCIE0:
	.long	0xffffffff
	.byte	0x1
	.string	""
	.uleb128 0x1
	.sleb128 -4
	.byte	0x8
	.byte	0xc
	.uleb128 0x4
	.uleb128 0x4
	.byte	0x88
	.uleb128 0x1
	.p2align 2
.LECIE0:
.LSFDE0:
	.long	.LEFDE0-.LASFDE0
.LASFDE0:
	.long	.Lframe0
	.long	.LFB3
	.long	.LFE3-.LFB3
	.byte	0x4
	.long	.LCFI0-.LFB3
	.byte	0xe
	.uleb128 0x8
	.byte	0x85
	.uleb128 0x2
	.byte	0x4
	.long	.LCFI1-.LCFI0
	.byte	0xd
	.uleb128 0x5
	.byte	0x4
	.long	.LCFI3-.LCFI1
	.byte	0x83
	.uleb128 0x4
	.byte	0x86
	.uleb128 0x3
	.byte	0x4
	.long	.LCFI4-.LCFI3
	.byte	0x2e
	.uleb128 0x10
	.p2align 2
.LEFDE0:
	.file 2 "/usr/include/stdio.h"
	.file 3 "/usr/include/sys/_types.h"
	.file 4 "/usr/include/machine/_types.h"
	.text
.Letext0:
	.section	.debug_info
	.long	0x326
	.value	0x2
	.long	.Ldebug_abbrev0
	.byte	0x4
	.uleb128 0x1
	.long	.Ldebug_line0
	.long	.Letext0
	.long	.Ltext0
	.long	.LASF37
	.byte	0x1
	.long	.LASF38
	.long	.LASF39
	.uleb128 0x2
	.long	.LASF0
	.byte	0x1
	.byte	0x6
	.uleb128 0x2
	.long	.LASF1
	.byte	0x1
	.byte	0x8
	.uleb128 0x2
	.long	.LASF2
	.byte	0x2
	.byte	0x5
	.uleb128 0x2
	.long	.LASF3
	.byte	0x2
	.byte	0x7
	.uleb128 0x3
	.string	"int"
	.byte	0x4
	.byte	0x5
	.uleb128 0x2
	.long	.LASF4
	.byte	0x4
	.byte	0x7
	.uleb128 0x4
	.long	.LASF11
	.byte	0x4
	.byte	0x3a
	.long	0x5a
	.uleb128 0x2
	.long	.LASF5
	.byte	0x8
	.byte	0x5
	.uleb128 0x2
	.long	.LASF6
	.byte	0x8
	.byte	0x7
	.uleb128 0x2
	.long	.LASF7
	.byte	0x4
	.byte	0x7
	.uleb128 0x2
	.long	.LASF8
	.byte	0x8
	.byte	0x4
	.uleb128 0x2
	.long	.LASF9
	.byte	0x1
	.byte	0x6
	.uleb128 0x2
	.long	.LASF10
	.byte	0x4
	.byte	0x5
	.uleb128 0x4
	.long	.LASF12
	.byte	0x3
	.byte	0x32
	.long	0x4f
	.uleb128 0x2
	.long	.LASF4
	.byte	0x4
	.byte	0x7
	.uleb128 0x4
	.long	.LASF13
	.byte	0x2
	.byte	0x2f
	.long	0x84
	.uleb128 0x5
	.long	0xca
	.long	.LASF16
	.byte	0x8
	.byte	0x2
	.byte	0x46
	.uleb128 0x6
	.long	.LASF14
	.byte	0x2
	.byte	0x47
	.long	0xca
	.byte	0x2
	.byte	0x23
	.uleb128 0x0
	.uleb128 0x6
	.long	.LASF15
	.byte	0x2
	.byte	0x48
	.long	0x41
	.byte	0x2
	.byte	0x23
	.uleb128 0x4
	.byte	0x0
	.uleb128 0x7
	.byte	0x4
	.long	0x2c
	.uleb128 0x5
	.long	0x1f8
	.long	.LASF17
	.byte	0x58
	.byte	0x2
	.byte	0x66
	.uleb128 0x8
	.string	"_p"
	.byte	0x2
	.byte	0x67
	.long	0xca
	.byte	0x2
	.byte	0x23
	.uleb128 0x0
	.uleb128 0x8
	.string	"_r"
	.byte	0x2
	.byte	0x68
	.long	0x41
	.byte	0x2
	.byte	0x23
	.uleb128 0x4
	.uleb128 0x8
	.string	"_w"
	.byte	0x2
	.byte	0x69
	.long	0x41
	.byte	0x2
	.byte	0x23
	.uleb128 0x8
	.uleb128 0x6
	.long	.LASF18
	.byte	0x2
	.byte	0x6a
	.long	0x33
	.byte	0x2
	.byte	0x23
	.uleb128 0xc
	.uleb128 0x6
	.long	.LASF19
	.byte	0x2
	.byte	0x6b
	.long	0x33
	.byte	0x2
	.byte	0x23
	.uleb128 0xe
	.uleb128 0x8
	.string	"_bf"
	.byte	0x2
	.byte	0x6c
	.long	0xa1
	.byte	0x2
	.byte	0x23
	.uleb128 0x10
	.uleb128 0x6
	.long	.LASF20
	.byte	0x2
	.byte	0x6d
	.long	0x41
	.byte	0x2
	.byte	0x23
	.uleb128 0x18
	.uleb128 0x6
	.long	.LASF21
	.byte	0x2
	.byte	0x70
	.long	0x1f8
	.byte	0x2
	.byte	0x23
	.uleb128 0x1c
	.uleb128 0x6
	.long	.LASF22
	.byte	0x2
	.byte	0x71
	.long	0x20a
	.byte	0x2
	.byte	0x23
	.uleb128 0x20
	.uleb128 0x6
	.long	.LASF23
	.byte	0x2
	.byte	0x72
	.long	0x230
	.byte	0x2
	.byte	0x23
	.uleb128 0x24
	.uleb128 0x6
	.long	.LASF24
	.byte	0x2
	.byte	0x73
	.long	0x250
	.byte	0x2
	.byte	0x23
	.uleb128 0x28
	.uleb128 0x6
	.long	.LASF25
	.byte	0x2
	.byte	0x74
	.long	0x27b
	.byte	0x2
	.byte	0x23
	.uleb128 0x2c
	.uleb128 0x8
	.string	"_ub"
	.byte	0x2
	.byte	0x77
	.long	0xa1
	.byte	0x2
	.byte	0x23
	.uleb128 0x30
	.uleb128 0x9
	.long	.LASF40
	.byte	0x1
	.uleb128 0x6
	.long	.LASF26
	.byte	0x2
	.byte	0x78
	.long	0x281
	.byte	0x2
	.byte	0x23
	.uleb128 0x38
	.uleb128 0x8
	.string	"_ur"
	.byte	0x2
	.byte	0x79
	.long	0x41
	.byte	0x2
	.byte	0x23
	.uleb128 0x3c
	.uleb128 0x6
	.long	.LASF27
	.byte	0x2
	.byte	0x7c
	.long	0x287
	.byte	0x2
	.byte	0x23
	.uleb128 0x40
	.uleb128 0x6
	.long	.LASF28
	.byte	0x2
	.byte	0x7d
	.long	0x297
	.byte	0x2
	.byte	0x23
	.uleb128 0x43
	.uleb128 0x8
	.string	"_lb"
	.byte	0x2
	.byte	0x80
	.long	0xa1
	.byte	0x2
	.byte	0x23
	.uleb128 0x44
	.uleb128 0x6
	.long	.LASF29
	.byte	0x2
	.byte	0x83
	.long	0x41
	.byte	0x2
	.byte	0x23
	.uleb128 0x4c
	.uleb128 0x6
	.long	.LASF30
	.byte	0x2
	.byte	0x84
	.long	0x96
	.byte	0x2
	.byte	0x23
	.uleb128 0x50
	.byte	0x0
	.uleb128 0xa
	.byte	0x4
	.uleb128 0xb
	.long	0x20a
	.byte	0x1
	.long	0x41
	.uleb128 0xc
	.long	0x1f8
	.byte	0x0
	.uleb128 0x7
	.byte	0x4
	.long	0x1fa
	.uleb128 0xb
	.long	0x22a
	.byte	0x1
	.long	0x41
	.uleb128 0xc
	.long	0x1f8
	.uleb128 0xc
	.long	0x22a
	.uleb128 0xc
	.long	0x41
	.byte	0x0
	.uleb128 0x7
	.byte	0x4
	.long	0x76
	.uleb128 0x7
	.byte	0x4
	.long	0x210
	.uleb128 0xb
	.long	0x250
	.byte	0x1
	.long	0x96
	.uleb128 0xc
	.long	0x1f8
	.uleb128 0xc
	.long	0x96
	.uleb128 0xc
	.long	0x41
	.byte	0x0
	.uleb128 0x7
	.byte	0x4
	.long	0x236
	.uleb128 0xb
	.long	0x270
	.byte	0x1
	.long	0x41
	.uleb128 0xc
	.long	0x1f8
	.uleb128 0xc
	.long	0x270
	.uleb128 0xc
	.long	0x41
	.byte	0x0
	.uleb128 0x7
	.byte	0x4
	.long	0x276
	.uleb128 0xd
	.long	0x76
	.uleb128 0x7
	.byte	0x4
	.long	0x256
	.uleb128 0x7
	.byte	0x4
	.long	0x18f
	.uleb128 0xe
	.long	0x297
	.long	0x2c
	.uleb128 0xf
	.long	0x8f
	.byte	0x2
	.byte	0x0
	.uleb128 0xe
	.long	0x2a7
	.long	0x2c
	.uleb128 0xf
	.long	0x8f
	.byte	0x0
	.byte	0x0
	.uleb128 0x4
	.long	.LASF31
	.byte	0x2
	.byte	0x85
	.long	0xd0
	.uleb128 0x10
	.long	0x302
	.byte	0x1
	.long	.LASF41
	.byte	0x1
	.byte	0x21
	.byte	0x1
	.long	0x41
	.long	.LFB3
	.long	.LFE3
	.byte	0x1
	.byte	0x55
	.uleb128 0x11
	.long	.LASF32
	.byte	0x1
	.byte	0x20
	.long	0x41
	.byte	0x2
	.byte	0x91
	.sleb128 8
	.uleb128 0x11
	.long	.LASF33
	.byte	0x1
	.byte	0x20
	.long	0x302
	.byte	0x1
	.byte	0x56
	.uleb128 0x12
	.long	.LASF34
	.byte	0x1
	.byte	0x22
	.long	0x308
	.byte	0x1
	.byte	0x53
	.uleb128 0x13
	.string	"ch"
	.byte	0x1
	.byte	0x23
	.long	0x41
	.byte	0x1
	.byte	0x50
	.byte	0x0
	.uleb128 0x7
	.byte	0x4
	.long	0x22a
	.uleb128 0x7
	.byte	0x4
	.long	0x2a7
	.uleb128 0x14
	.long	.LASF35
	.byte	0x2
	.byte	0x8b
	.long	0x308
	.byte	0x1
	.byte	0x1
	.uleb128 0x15
	.long	.LASF36
	.byte	0x2
	.value	0x1a4
	.long	0x41
	.byte	0x1
	.byte	0x1
	.byte	0x0
	.section	.debug_abbrev
	.uleb128 0x1
	.uleb128 0x11
	.byte	0x1
	.uleb128 0x10
	.uleb128 0x6
	.uleb128 0x12
	.uleb128 0x1
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x25
	.uleb128 0xe
	.uleb128 0x13
	.uleb128 0xb
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x1b
	.uleb128 0xe
	.byte	0x0
	.byte	0x0
	.uleb128 0x2
	.uleb128 0x24
	.byte	0x0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3e
	.uleb128 0xb
	.byte	0x0
	.byte	0x0
	.uleb128 0x3
	.uleb128 0x24
	.byte	0x0
	.uleb128 0x3
	.uleb128 0x8
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3e
	.uleb128 0xb
	.byte	0x0
	.byte	0x0
	.uleb128 0x4
	.uleb128 0x16
	.byte	0x0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.byte	0x0
	.byte	0x0
	.uleb128 0x5
	.uleb128 0x13
	.byte	0x1
	.uleb128 0x1
	.uleb128 0x13
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.byte	0x0
	.byte	0x0
	.uleb128 0x6
	.uleb128 0xd
	.byte	0x0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x38
	.uleb128 0xa
	.byte	0x0
	.byte	0x0
	.uleb128 0x7
	.uleb128 0xf
	.byte	0x0
	.uleb128 0xb
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.byte	0x0
	.byte	0x0
	.uleb128 0x8
	.uleb128 0xd
	.byte	0x0
	.uleb128 0x3
	.uleb128 0x8
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x38
	.uleb128 0xa
	.byte	0x0
	.byte	0x0
	.uleb128 0x9
	.uleb128 0x13
	.byte	0x0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3c
	.uleb128 0xc
	.byte	0x0
	.byte	0x0
	.uleb128 0xa
	.uleb128 0xf
	.byte	0x0
	.uleb128 0xb
	.uleb128 0xb
	.byte	0x0
	.byte	0x0
	.uleb128 0xb
	.uleb128 0x15
	.byte	0x1
	.uleb128 0x1
	.uleb128 0x13
	.uleb128 0x27
	.uleb128 0xc
	.uleb128 0x49
	.uleb128 0x13
	.byte	0x0
	.byte	0x0
	.uleb128 0xc
	.uleb128 0x5
	.byte	0x0
	.uleb128 0x49
	.uleb128 0x13
	.byte	0x0
	.byte	0x0
	.uleb128 0xd
	.uleb128 0x26
	.byte	0x0
	.uleb128 0x49
	.uleb128 0x13
	.byte	0x0
	.byte	0x0
	.uleb128 0xe
	.uleb128 0x1
	.byte	0x1
	.uleb128 0x1
	.uleb128 0x13
	.uleb128 0x49
	.uleb128 0x13
	.byte	0x0
	.byte	0x0
	.uleb128 0xf
	.uleb128 0x21
	.byte	0x0
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2f
	.uleb128 0xb
	.byte	0x0
	.byte	0x0
	.uleb128 0x10
	.uleb128 0x2e
	.byte	0x1
	.uleb128 0x1
	.uleb128 0x13
	.uleb128 0x3f
	.uleb128 0xc
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x27
	.uleb128 0xc
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x11
	.uleb128 0x1
	.uleb128 0x12
	.uleb128 0x1
	.uleb128 0x40
	.uleb128 0xa
	.byte	0x0
	.byte	0x0
	.uleb128 0x11
	.uleb128 0x5
	.byte	0x0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0xa
	.byte	0x0
	.byte	0x0
	.uleb128 0x12
	.uleb128 0x34
	.byte	0x0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0xa
	.byte	0x0
	.byte	0x0
	.uleb128 0x13
	.uleb128 0x34
	.byte	0x0
	.uleb128 0x3
	.uleb128 0x8
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x2
	.uleb128 0xa
	.byte	0x0
	.byte	0x0
	.uleb128 0x14
	.uleb128 0x34
	.byte	0x0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0xb
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x3f
	.uleb128 0xc
	.uleb128 0x3c
	.uleb128 0xc
	.byte	0x0
	.byte	0x0
	.uleb128 0x15
	.uleb128 0x34
	.byte	0x0
	.uleb128 0x3
	.uleb128 0xe
	.uleb128 0x3a
	.uleb128 0xb
	.uleb128 0x3b
	.uleb128 0x5
	.uleb128 0x49
	.uleb128 0x13
	.uleb128 0x3f
	.uleb128 0xc
	.uleb128 0x3c
	.uleb128 0xc
	.byte	0x0
	.byte	0x0
	.byte	0x0
	.section	.debug_pubnames,"",@progbits
	.long	0x17
	.value	0x2
	.long	.Ldebug_info0
	.long	0x32a
	.long	0x2b2
	.string	"main"
	.long	0x0
	.section	.debug_aranges,"",@progbits
	.long	0x1c
	.value	0x2
	.long	.Ldebug_info0
	.byte	0x4
	.byte	0x0
	.value	0x0
	.value	0x0
	.long	.Ltext0
	.long	.Letext0-.Ltext0
	.long	0x0
	.long	0x0
	.section	.debug_str,"MS",@progbits,1
.LASF34:
	.string	"bfile"
.LASF20:
	.string	"_lbfsize"
.LASF16:
	.string	"__sbuf"
.LASF2:
	.string	"short int"
.LASF10:
	.string	"long int"
.LASF26:
	.string	"_extra"
.LASF17:
	.string	"__sFILE"
.LASF37:
	.string	"GNU C 3.4.2 [FreeBSD] 20040728"
.LASF39:
	.string	"/home/pete/project/yasm3/yasm"
.LASF21:
	.string	"_cookie"
.LASF28:
	.string	"_nbuf"
.LASF25:
	.string	"_write"
.LASF31:
	.string	"FILE"
.LASF5:
	.string	"long long int"
.LASF11:
	.string	"__int64_t"
.LASF29:
	.string	"_blksize"
.LASF22:
	.string	"_close"
.LASF33:
	.string	"argv"
.LASF27:
	.string	"_ubuf"
.LASF1:
	.string	"unsigned char"
.LASF23:
	.string	"_read"
.LASF32:
	.string	"argc"
.LASF36:
	.string	"__isthreaded"
.LASF0:
	.string	"signed char"
.LASF40:
	.string	"__sFILEX"
.LASF6:
	.string	"long long unsigned int"
.LASF4:
	.string	"unsigned int"
.LASF3:
	.string	"short unsigned int"
.LASF41:
	.string	"main"
.LASF14:
	.string	"_base"
.LASF19:
	.string	"_file"
.LASF9:
	.string	"char"
.LASF13:
	.string	"fpos_t"
.LASF7:
	.string	"long unsigned int"
.LASF35:
	.string	"__stderrp"
.LASF12:
	.string	"__off_t"
.LASF24:
	.string	"_seek"
.LASF8:
	.string	"double"
.LASF30:
	.string	"_offset"
.LASF38:
	.string	"test_hd.c"
.LASF18:
	.string	"_flags"
.LASF15:
	.string	"_size"
	.ident	"GCC: (GNU) 3.4.2 [FreeBSD] 20040728"
