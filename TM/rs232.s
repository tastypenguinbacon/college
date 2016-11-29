.ORG    0h
        LJMP    INIT
.ORG    30h
INIT:   MOV     TMOD,   #0010000b   ;ustawia timer1 w tryb pracy ośmiobitowej
        SETB    EA  ; zezwolenie na przerwania
        SETB    ES  ; zezwolenie na przerwania od transmisji
        ANL     0x87,   #0x7f   ;wyłącza SMOD, baudrate = oscylator/(384[256-TH1])
        MOV     TH1,    #jakaś_liczba_wyliczona_z_powyższego
        MOV     SCON,   ;8-bitowy tryb komunikacji taktowany zegarem, możliwe odbieranie
        MOV     TMOD,   #0x20
        SETB    TR1
        
SEND:   MOV     SBUF, #to co wysyłamy
        LCALL   TIMER
        SJMP    SEND
        
TIMER:  clr TR0 ;   tutaj poprawić
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