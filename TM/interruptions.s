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

Laboratorium godzina 12:30, wtorek - Adrian Jałoszewski, układ 8051

Kod zapalający wszystkie diody:
org 0
    LJMP start
org 30h
start:
    mov P0,#0x00
    mov P1,#0x00
    mov P2,#0x00
    mov P3,#0x00
loop:
    LJMP loop
end


Kod migoczący na opóźnieniu pętlami około 3 Hz:

org 0
LJMP start

org 30h
start:
    mov A, #00h
loop:
    mov R0, #20
loop1:
    mov R1, #50
loop2:
    mov R2, #70
loop3:
    djnz R2, loop3
    djnz R1, loop2
    djnz R0, loop1
    xrl A, #0FFh
    mov P0, A
    sjmp loop

Kod układu zapalającego diodę z okresem 20ms
.ORG 0
    ljmp main
.ORG 0x0B
    ljmp timer

.ORG 0x030
main:
    mov TMOD, #0x1 ; initializing the timer
    mov IE, #0x82
    mov TH0, #0xbe ; hex(2**16-20000*10/12) - python, pierwszy bajt tu
    mov TL0, #0xe6 ; drugi bajt tu
    setb TR0
    jmp $
timer:
    clr TR0
    mov TH0, #0xbe
    mov TL0, #0xe6
    setb TR0
    xrl A, #0xFF
    mov P0, A
    reti
END

Dokładnie ten sam kod co poprzednio tyle, że dioda jest zapalana tylko co 50 przerwanie - 50
* 20ms = 1s

timer:
    clr TR0
    mov TH0, #0xbe
    mov TL0, #0xe6
    setb TR0
    djnz R1, once_a_second ; skips every 50th
    mov R1, #50
    xrl A, #0xFF
    mov P0, A
    reti
once_a_second:
    reti
END