bits 64
default rel

section .text

global check_age

check_age:
    cmp rcx, 18
    jg .accepted

    lea rax, [rel rejected]
    ret

.accepted:
    lea rax, [rel accepted]
    ret


section .rdata

accepted:
    db "Allowed to drink! yay!", 0

rejected:
    db "Not allowed to drink! arrest him!", 0
