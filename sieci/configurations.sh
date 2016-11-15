# ważne uwagi wstępne: 
1.) CLI w Cisco ma autouzupełnienia - jeżeli wpiszesz wystarczająco, to może być dany biały znak
2.) Jeżeli dasz w CLI Cisco "?" po jakiejś komendzie, to wskaże ci możliwe uzupełnienia
3.) tabulator uzupełnia tekst do pełnej formy, jeżeli ta jest w pełni jednoznaczna
4.) Komendy Cisco mają głęboko gdzieś wielkość liter dopóki to nie nazwy własne (jak chociażby hasło albo nazwa hosta) 
5.) Podawnie numerków po przecinku - suma przedziałów
6.) Podawanie numerków z myślnikiem i spacjami po bokach (number - number) - przedział

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
Kwiatek# show running-config                    # pokazuje aktualną konfigurację

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
Kwiatek(config)# interface range fa 0/15 - 17   #spacje konieczne, pozwala na konfigurowanie całego zakresu interfejsów na raz

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

# Klasyczna metoda modyfikowania VLANów
Kwiatek# vlan database  # może już ogólnie być niewspierane, ale w ten sposób za dinozaurów się to robiło

# VLAN trunks z następujących przykładów będą używały enkapsulacji IEEE 802.1Q
Kwiatek(config) interface fa 0/1
Kwiatek(config-if) switchport trunk encapsulation dot1q    # w niektórych do działania konieczne jest ręczne ustawienie
Kwiatek(config-if) switchport mode trunk    #   ustawia tryb na trunkowanie - wyłącza dynamica
Kwiatek(config-if) switchport trunk allowed vlan 1-100  # chyba nie muszę tłumaczyć co to robi, tutaj jeszcze nie działa, potrzebna enkapsulacja
Kwiatek(config-if) switchport trunk allowed vlan remove 10  # też zdaje się być trywialne 

# metody pozwalające sprawdzić stan trunka i vlanów
Kwiatek# show vlan
Kwiatek# show interface trunk               
Kwiatek# show interface fa 0/1 switchport
Kwiatek# show interface fa 0/1 status 

# native vlan to taki VLAN jaki jest wybierany przy braku enkapsulacji (domyślnie jest to VLAN 1)
Kwiatek(config)# int fa 0/1
Kwiatek(config-if)# switchport trunk native vlan 10 # zmieniamy native VLAN

# VTP - (Virtual LAN Trunking Protocol) - automatyczna propagacja informacji o VLANach
# aby działał poprawnie po drodze nie może być switchy innych firm ani switchy z innych VTP
# server, transparent, client - serwuje dla clientów, forwarduje, odbiera od serwera
# gdy przełącznik dołącza do domeny VTP, pobiera automatycznie bazę VLAN od istniejących switchy (nawet jeżeli będzie serwerem)
# łącza muszą być skonfigurowane jako trunki
# w przełącznikach należy dać taką samą nazwę domeny
Kwiatek(config)# vtp domain "nazwa domeny"
Kwiatek(config)# vtp password "coś tajnego" # zabezpiecza urządzenia z VTP hasłem, muszą być jednolite w ramach VTP
Kwiatek# show vtp status
Kwiatek#debug sw-vlan vtp events    # diagnostyka

# konfigurowanie VTP client
Kwiatek(config)# vtp domain domena
Kwiatek(config)# vtp mode client

# konfigurowanie VTP serwer - należy najpierw utworzyć tam kilka VLANów, uwasa - propagacja info o nowym vlanie dopiero po exit
# konieczne jest stworzenie kilka VLANów, a nie interfejsów VLAN
Kwiatek(config)# vlan 50
# bazowa ilość VLAN to 5, tworzenie nowych zwiększa tę liczbę
Kwiatek(config)# vtp mode transparent   # ustawienie vtp jako transparendt
Kwiatek(config)# vtp mode server        # guess what
