.ORG 0
    JMP     start
    
.ORG 0BH
    JMP     interrupted_by_timer

.ORG 030H
start:
    MOV     TMOD,   #1  ; set timer mode to 16 bits
    MOV     TL0,    #0FFh
    MOV     TH0,    #0FFh 
    MOV     EA,     #1  ; enable global interrupts
    SETB    TR0         ; start timer 0
    JMP     $           ; whie (true)
interrupted_by_timer:
    CLR     TR0
    MOV     TL0     #0FFh
    MOV     TH0     #0FFh
    XRL     A,      #0FFh
    MOV     P0,     A
    RETI
