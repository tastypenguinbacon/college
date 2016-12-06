.ORG    0h
        LJMP    INIT
.ORG    023h
        LJMP    SERIAL
        
.ORG    30h
INIT:   MOV     TMOD,   #20     ;tIMER 1, MODE 2(AUTO RELOAD)
        MOV     TH1,    #-6     ;4800 baud rate
        MOV     SCON,   #50     ;8-BIT, 1 stop, REN enabled
        SETB    TR1             ;start timer
MAIN:   
        SJMP    MAIN
FOREVER:SJMP    FOREVER         ; interruption based

SERIAL: MOV     SBUF,   A       ; załaduj akumulatordo SBUF
WAIT:   JNB     TI,     HERE    ; wait for last bit to transfer
        CLR     TI              ; get ready for next byte
        RET

;http://what-when-how.com/8051-microcontroller/8051-serial-port-programming-in-assembly/


