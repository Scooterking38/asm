bits 64
default rel

cmp rcx, 18
jg .accepted

lea rax, [rejected]
ret

.accepted:
lea rax, [accepted]
ret


accepted:
    db "Allowed to drink! yay!", 0

rejected:
    db "Not allowed to drink! arrest him!", 0
