# ważne elementy składniowe:
do  # pozwala na wykonanie czegoś tak jakby się nie weszło w konfiguracje
no  # wyłącza daną opcję w konfiguracji

# najważniejsze komendy jakie istnieją w routerach Cisco
Kwiatek> enable             # przechodzi do trybu uprawnionego (tj. sudo) 
Kwiatek# configure terminal # wchodzi do ustaień
Kwiatek(config)# hostname "nazwa hosta" # ustawia nazwę hosta na zadaną 

# wyłączenie stronicowania i innych nieznośnych opcji
Kwiatek# terminal length 0  # wyłącza stronicowanie
Kwiatek(config)# no ip domain-lookup    # wyłącza wyszukiwanie domeny jak źle wpiszemy komendę, działa tylko na ruterach
Kwiatek(config)# no service config      # nie pobiera konfiguracji przez TFTP - tyko NVRAM lub wcale

# konfigurowanie interfejsu FastEthernet
Kwiatek(config)# interface FastEthernet 0/1 # wchodzimy do konfiguracji interfejsu podanego pod danym numerkiem (są wytłoczone na obudowie)
Kwiatek(config-if)# no shutdown # włącza dany interfejs

# sprawdzanie ustawień
Kwiatek# show ip interface brief    # pokazuje wszystkie włączone porty
