reset #resetuje

dir flash:
boot flash:/plik_obrazu_IOS.bin	#flash
boot disk0:/plik_obrazu_IOS.bin #linear flash (adresowanie linowe)
boot slot0:/plik_obrazu_IOS.bin #ATA flash (z FAT)

enable #sudo

configure terminal #conf t

enable password "hasło" 
ip http server #uruchomienie serwera HTTP 
ip http secure-server #uruchomienie serwera HTTPS
ip http authentication local 
username "tutaj jakiś usernejm" privilege "przywilej" password 0 "hasło" #nowy użytkowinik, max przywilej, hasło
line console 0
	login local
exit
line vty 0 4
	privilege level 15 #prawo do edycji linii mają tylko ci z 15
	login local #autoryzacja na podstawie sytemowej bazy użytkowników, a nie uniwersalnego hasła
	transport input telnet
exit

no ip domain-lookup #wyłącza klienta DNS
no service config #nie pobiera configuracji przez TFTP - tylko NVRAM lub wcale
terminal length 0 #wyłączenie stronicowania przy wypisywaniu dłuższych raportów na konsoli

#konfiguracje są odpowiednio: startowa (w NVRAM) i bieżąca (aktualnie używana)
#
# Zapisywanie trwałe w NVRAM konfiguracji - nie wywoływać:
#   write mem                                             
# lub równoważne
#   copy running-config startup-config
# Następnie zlecić ponowne uruchomienie routera:
#	reload
# Kasowanie konfiguracji z NVRAM
#	write erase


configure terminal
interface serial 0/0

configure terminal
interface FastEthernet 0/1
ip address "jakiś ip" "jakaś maska"
no shutdown

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

#definiowanie nazwy hosta
hostname "nazwa hosta"
#stan interfejsów
show ip interface brief
show interfaces description
logging console 2 #filtrowanie poziomów logowania (łącznie jest ich 8)
show running-config #bieżąca konfiguracja
show startup-config #konfiguracja w NVRAM

#zalogowani użytkownicy i ich sesje
sh users
sh sessions

#diagonostyka ICMP/ping
ping "adres ip" rep "liczba powtórzeń" #niektóre mają możliwość pingowania broadcastowego
# CTRL+SHIFT+6 - anulowanie procesu
# najs to know - można w łatwy sposób skracać robotę - liczą się tylko przedrostki, jeżeli jest już unikatowe, to nie trzeba kończyć komendy 

#testowanie funkcjonowania protokołu CDP (Cisco Discovery Protocol)
