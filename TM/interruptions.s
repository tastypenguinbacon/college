.ORG 0
    LJMP    main

.ORG 0x03
    LJMP    change
    
.ORG 0x0B
    LJMP    timer

.ORG 0x30
main:
    SETB    EA
    SETB    ET0
    SETB    TR0
    MOV     R1,      #0x7f
    MOV     TL0,     R1
    SETB    IT0
    JMP     $
    
timer:
    CJNE    P1,     #1,     zero_value
one_value:
    CLR     TR0
    MOV     P1,     #0
    MOV     TL0,    R1
    SETB    TR0
    RETI
zero_value:
    CLR     TR0
    MOV     P1,     #1
    MOV     A,      #Oxff
    SUBB    A,      R1
    MOV     TL0,    A
    SETB    TR0
    RETI
    
change:
    CLR     EA
    INC     R1
    SETB    EA
    RETI
END