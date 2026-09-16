bits 64
default rel

section .text

global check_age

check_age:
    cmp rcx, 18
    jg .accepted

    mov rax 0
    ret

.accepted:
    mov rax, 1
    ret
