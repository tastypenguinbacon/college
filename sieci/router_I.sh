reset # resetuje

dir flash:
boot flash:/plik_obrazu_IOS.bin	# flash
boot disk0:/plik_obrazu_IOS.bin # linear flash (adresowanie linowe)
boot slot0:/plik_obrazu_IOS.bin # ATA flash (z FAT)

enable # sudo

configure terminal # conf t

(config)# enable password "hasło" 
(config)# ip http server # uruchomienie serwera HTTP 
(config)# ip http secure-server #u ruchomienie serwera HTTPS
(config)# ip http authentication local 
(config)# username "tutaj jakiś usernejm" privilege "przywilej" password 0 "hasło" #nowy użytkowinik, max przywilej, hasło
line console 0
	login local
exit
line vty 0 4
	privilege level 15 # prawo do edycji linii mają tylko ci z 15
	login local # autoryzacja na podstawie sytemowej bazy użytkowników, a nie uniwersalnego hasła
	transport input telnet
exit

(config)# no ip domain-lookup #wyłącza klienta DNS
(config)# no service config #nie pobiera configuracji przez TFTP - tylko NVRAM lub wcale
terminal length 0 #wyłączenie stronicowania przy wypisywaniu dłuższych raportów na konsoli

# konfiguracje są odpowiednio: startowa (w NVRAM) i bieżąca (aktualnie używana)
#
# Zapisywanie trwałe w NVRAM konfiguracji - nie wywoływać:
#   write mem                                             
# lub równoważne
#   copy running-config startup-config
# Następnie zlecić ponowne uruchomienie routera:
#	reload
# Kasowanie konfiguracji z NVRAM
#	write erase


(config)# interface serial 0/0

(config)# interface FastEthernet 0/1
(config-if)# ip address "jakiś ip" "jakaś maska"
(config-if)# no shutdown

# budowanie interfejsów wirtualnych
interface Loopback 0
ip address "jakiś ip" "jakaś maska"
no shutdown

#sprawdzanie ustawień i stanów interfejsów
show ip int fa 0/1
show interfaces summary
show interfaces fa 0/1 summary
show interfaces descrition 
show interfaces accounting
show interfaces fa 0/1 accounting
show interfaces fa 0/1 
show controllers fa 0/1
show run

# definiowanie nazwy hosta
(config)# hostname "nazwa hosta"
# stan interfejsów
show ip interface brief
show interfaces description
(config)# logging console 2 #filtrowanie poziomów logowania (łącznie jest ich 8)
show running-config #bieżąca konfiguracja
show startup-config #konfiguracja w NVRAM

# zalogowani użytkownicy i ich sesje
sh users
sh sessions

# diagonostyka ICMP/ping
ping "adres ip" rep "liczba powtórzeń" #niektóre mają możliwość pingowania broadcastowego
# CTRL+SHIFT+6 - anulowanie procesu
# najs to know - można w łatwy sposób skracać robotę - liczą się tylko przedrostki, jeżeli jest już unikatowe, to nie trzeba kończyć komendy 

# testowanie funkcjonowania protokołu CDP (Cisco Discovery Protocol)
# podłączyć do dowolnego interfejsu routera interfejs drugiego routera i skonfiguruj je
sh cdp
sh cdp neighbors
sh cdp neighbors detail
# Wyłączenie/włączenie cdp
(config)# no cdp run
(config)# cdp run 
# wyłączenie cdp w konkretnym interfejsie 
(config)# interface fa 0/1
(config)# no cdp enable
# sprawdzenie cdp dla interfejsów
sh cdp interfaces
# kasowanie zawartości talbicy z inforamcjami o innych urządzeniach zgromadzonymi przez cdp
clear cdp table 
# Konfigurowanie prędkości i czasu aktualności komunikatu CDP (w sekundach) 
(config)# cdp timer 10
(config)# cdp holdtime 90
# należy zmienić parametry prędkości nadawania i czasu aktualności o obydwu 
# routerach, następnie w jednym z nich dać nową nazwą hosta, 
# obserwując czas rozpropagowania info przy pomocy CDP
(config)# hostname "jakaś nazwa hosta"
show cdp neighbors


# Konfigurowanie serwera DHCP
# 1.) skonfigurować i włączyć interfejsy rutera R1 - projektując IP zgodnie z zasadami
# 2.) Włączyć DHCP
(dhcp-config)# service dhcp
(dhcp-config)# ip dhcp pool "nazwa puli adresów" #tutaj konfigurujemy DHCP
(dhcp-config)# network "jakiś IP" "jakaś maska"
(dhcp-config)# default-router "jakiś inny IP"
(dhcp-config)# dns-server 123.123.123.3 #nie wiem czy nie powinien być inny
(dhcp-config)# domain-name "jakaś nazwa domen"
(config) ip dhcp excluded-address "jakiś ip" "jakiś inny ip" # drugi był większy niż pierwszy, więc może to ma znaczenie
# Uwaga - pula adresów DHCP i adres interfejsu rutera mprzez który mbędzie prowadzone konfigurowanie muszą być w tej samej sieci - to właśnie w tej sieci będą przydzielane adresy IP (stąd konieczna jest zbieżność).
# dla powyższego przykładu może to być adres (config-if)ip addr 10.10.10.1 255.255.255.0
# i wtedy ten adres IP jest jednocześnie adresem domyślnej bramki z sieci

# należy analogicznie stworzyć drugą pulę DHCP
# Interfejsy stacji PC oraz podłączony do R1 interfejs rutera R2 należy
# skonfigurować do trybu klient DHCP (automatycznie uzyskiwanie adresu IP):
(config)# interface fa 0/0
(config-if)# ip address dhcp
# sprawdzenie w routerze R1 stanu serwera DHCP
show ip dhcp binding
# diagnostyka
debug ip dhcp server events
# zdalne DHCP (nie musi być bezpośrednie połączenie - każdy ruter musi przepuścić zapytania DHCP)
(config-if) ip helper-address "ip kolejnego rutera na trasie do serwera"
# powróć do adresacji statycznej

# mostki - bez foci нет 
