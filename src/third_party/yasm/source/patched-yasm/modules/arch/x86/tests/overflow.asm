[bits 16]
mov ax, 'abcd'
mov ax, 0x1ffff
mov eax, 0x111111111

dd 0x123456789
dd -1
dw 0x12345
dw -1

jmp 0x1234:0x56789ABC
jmp dword 0x1234:0x56789ABC
