section .text
    MOV EAX, 21
    MOV EBX, 28
whi:
    CMP EAX, EBX
    JE fin
    JLE els
    SUB EAX, EBX ; mov ax, 5
    CALL od
    MOV EAX, 2
    MOV EBX, 2
    JMP whi
els:
    SUB EBX, EAX ; mov bx, 5
od: 
    CALL whi
    MOV EAX, 3
    MOV EBX, 3
    JMP whi
fin: 
    HLT