section .text
    CALL _start
    HLT

f: 
    CMP ECX, 0
    JG els
    SUB ESI, ESP
    RET

els: 
    SUB ECX, 1
    CALL f
    MOV EDX, EAX
    ADD EDX, EBX
    MOV EAX, EBX
    MOV EBX, EBX
    RET

_start:
    MOV ECX, 5
    MOV EBX, 1
    MOV EBX, 1
    MOV ESI, ESP
    CALL f
    RET