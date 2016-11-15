# ważne uwagi wstępne: 
1.) CLI w Cisco ma autouzupełnienia - jeżeli wpiszesz wystarczająco, to może być dany biały znak
2.) Jeżeli dasz w CLI Cisco "?" po jakiejś komendzie, to wskaże ci możliwe uzupełnienia
3.) tabulator uzupełnia tekst do pełnej formy, jeżeli ta jest w pełni jednoznaczna
4.) Komendy Cisco mają głęboko gdzieś wielkość liter dopóki to nie nazwy własne (jak chociażby hasło albo nazwa hosta) 

# ważne elementy składniowe:
do  # pozwala na wykonanie czegoś tak jakby się nie weszło w konfiguracje
no  # wyłącza daną opcję w konfiguracji

# najważniejsze komendy jakie istnieją w routerach Cisco
Kwiatek> enable             # przechodzi do trybu uprawnionego (tj. sudo) 
Kwiatek# configure terminal # wchodzi do ustaień
Kwiatek(config)# hostname "nazwa hosta"         # ustawia nazwę hosta na zadaną 
Kwiatek(config)# logging console "numer do 8"   # ustawia logowanie na tylko danym poziomie

# wyłączenie stronicowania i innych nieznośnych opcji
Kwiatek# terminal length 0  # wyłącza stronicowanie
Kwiatek(config)# no ip domain-lookup    # wyłącza wyszukiwanie domeny jak źle wpiszemy komendę, działa tylko na ruterach
Kwiatek(config)# no service config      # nie pobiera konfiguracji przez TFTP - tyko NVRAM lub wcale


# konfigurowanie interfejsu FastEthernet
Kwiatek(config)# interface FastEthernet 0/1 # wchodzimy do konfiguracji interfejsu podanego pod danym numerkiem (są wytłoczone na obudowie)
Kwiatek(config-if)# no shutdown # włącza dany interfejs

# sprawdzanie ustawień
Kwiatek# show ip interface brief                # pokazuje wszystkie interfejsy w sposób ogólny
Kwiatek# show ip interface FastEthernet 0/1     # pokaż interfejs w sposób szczegółowy - nie działa na switchu o dziwo
Kwiatek# show interfaces summary                # nie wiem dlaczego nie działa, było w Routerach
Kwiatek# show interfaces fa 0/1 summary         # też nie wiem dlaczego nie działa, też było w Routerach
Kwiatek# show interfaces accounting             # to samo
Kwiatek# show interfaces descrition             # może to literówka, ale nie mogę sprawdzić, bo jak powyżej
Kwiatek# show controllers                       # pokazuje strasznie dużo info, ale nie wiem po co 

# zalogowani użytkownicy i ich sesje
Kwiatek# show users
Kwiatek# show sessions


####################################################################################
#                                                                                  #
#                                FastEthernet                                      #
#                                                                                  #
####################################################################################

Kwiatek(config)# interface fa 0/1   # wchodzi do interfejsu FastEthernet 0/1 
Kwiatek(config-if)# switchport mode access  # access zmienia tryb interfejsu na komunikację z DTE, pozostałe możliwe to trunk (z DCE), dynamic (sam określa na podstawie obiektu po drugiej stronie)
Kwiatek(config-if)# switchport nonegotiate  # wyłącza DTP - Dynamic Trunking Protocol - ten co przydziela dynamic mode'a


####################################################################################
#                                                                                  #
#                                   VLAN                                           #
#                                                                                  #
####################################################################################

Kwiatek(config)# interface vlan "numerek vlana" # przechodzi do konfiguracji danego numerkiem Vlana
Kwiatek(config-if)# ip address  "jakiś adres ip" "jakaś maska"  # nadaje adres IP dla danego VLANa - pozwala to na logowanie się na VLANie - nadanie adresu pozwala 
Kwiatek(config-if)# no shutdown # włącza VLANa

Kwiatek# show interface vlan 1  # jak nazwa wskazuje

Kwiatek(config)# interface vlan 50  # tworzy nowy VLAN nr 50

# Przypisywanie portu pod VLAN
Kwiatek(config)# interface fa 0/1
Kwiatek(config-if)# switchport mode access 
Kwiatek(config-if)# switchport access vlan 50   # przypisanie portu do VLANa
