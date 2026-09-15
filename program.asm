bits 64
default rel

extern GetStdHandle
extern WriteFile
extern ExitProcess

section .text

global main

main:
    ; Choose the message.
    ; Change this value to test different ages.
    mov rcx, 19

    cmp rcx, 18
    jg .accepted

    lea rsi, [rejected]
    mov edx, rejected_len
    jmp .print

.accepted:
    lea rsi, [accepted]
    mov edx, accepted_len

.print:
    ; GetStdHandle(STD_OUTPUT_HANDLE)
    mov ecx, -11
    call GetStdHandle

    ; WriteFile(
    ;     stdout,
    ;     message,
    ;     length,
    ;     &written,
    ;     NULL
    ; )
    mov rcx, rax
    mov rdx, rsi
    ; r8d already contains length
    lea r9, [written]

    sub rsp, 32
    push 0
    call WriteFile
    add rsp, 40

    xor ecx, ecx
    call ExitProcess


section .data

accepted:
    db "Allowed to drink! yay!", 13, 10
accepted_len equ $ - accepted

rejected:
    db "Not allowed to drink! arrest him!", 13, 10
rejected_len equ $ - rejected

written:
    dd 0
