.ORG    0h
        LJMP    INIT
.ORG    0Bh
        LJMP    TIMER
.ORG    023h
        LJMP    SERIAL
        
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
        LCALL   SLEEP
        SJMP    SEND
        
SLEEP:  SETB    ET0
        MOV     R1,     #1
HERE:   CJNE    R1,     #0,     HERE
        CLR     ET0
        RET
TIMER:  
        MOV     R1      #0
        RETI
        
SERIAL: