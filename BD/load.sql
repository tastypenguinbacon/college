/*
 * Adrian Jałoszewski
 * jaloszewski.adrian@gmail.com
 */

INSERT INTO infrastruktura_telekomunikacyjna.miasto VALUES
  (0, 'Kopenhaga', 'Dania'),
  (1, 'Berlin', 'Niemcy'),
  (2, 'Wroclaw', 'Polska'),
  (3, 'Krakow', 'Polska'),
  (4, 'Warszawa', 'Polska'),
  (5, 'Hamburg', 'Niemcy'),
  (6, 'Rzym', 'Włochy');

INSERT INTO infrastruktura_telekomunikacyjna.miejsce_pracy VALUES
  (0, 3, 'Comarch', 'Jana Pawła II 39a'),
  (1, 1, 'Vodafone', 'Ferdinand-Braun-Platz 1'),
  (2, 6, 'Pasta-Telecom', 'Mario Mario Strada 2'),
  (3, 5, 'Vodafone', 'Amsinckstr. 59');

INSERT INTO infrastruktura_telekomunikacyjna.pracownik VALUES
  (0, 0, 'Adrian', 'Jałoszewski', 'jaloszewski.adrian@gmail.com'),
  (1, 1, 'Hans', 'Landa', 'hans.landa@vf.de'),
  (2, 3, 'Donny', 'Donowitz', 'dony.donowitz@vf.de'),
  (3, 2, 'Antonio', 'Gorlani', 'antonio.gorlani@mamamia.it');

INSERT INTO infrastruktura_telekomunikacyjna.producent VALUES
  (0, 'Cisco', 'cisco@cisco.com', 'www.cisco.com'),
  (1, 'Juniper', 'juniper@juniper.net', 'www.juniper.net');

INSERT INTO infrastruktura_telekomunikacyjna.produkt VALUES
  (0, 0, 'C881-K9', 'router'),
  (1, 0, 'Catalyst 2960-X', 'switch'),
  (2, 0, 'SG350-10', 'switch'),
  (3, 1, 'EXX4200', 'switch'),
  (4, 1, 'MX2KMPC9EQRB', 'core router');

INSERT INTO infrastruktura_telekomunikacyjna.urzadzenie VALUES
  (0, 0, 0, 'cisco-r-1'),
  (1, 1, 0, 'cisco-s-1'),
  (2, 1, 2, 'cisco-s-2'),
  (3, 2, 3, 'cisco-s-3'),
  (4, 3, 4, 'jun-s-1'),
  (5, 4, 1, 'jun-cr-1'),
  (6, 2, 3, 'cisco-s-4'),
  (7, 3, 5, 'jun-s-2'),
  (8, 4, 6, 'jun-cr-2');

INSERT INTO infrastruktura_telekomunikacyjna.metryka VALUES
  (0, 'liczba', 'gubione pakiety na godzinę'),
  (1, 'procent', 'downtime w poprzednim miesiącu'),
  (2, 'milisekundy', 'ping z Berlina');

INSERT INTO infrastruktura_telekomunikacyjna.wartosc_metryki VALUES
  (0, 0, 2, '2017-12-1 10:23:54', 10),
  (1, 0, 2, '2017-12-1 10:23:55', 12),
  (2, 0, 2, '2017-12-1 10:23:56', 9),
  (3, 1, 1, '2017-11-1 00:00:00', 0.1),
  (4, 1, 1, '2017-12-1 00:00:00', 0.001),
  (5, 1, 5, '2017-11-1 00:00:00', 0.1),
  (6, 1, 5, '2017-12-1 00:00:00', 0.001);

INSERT INTO infrastruktura_telekomunikacyjna.awaria VALUES
  (0, 'fail-1', NULL, NULL, '2017-12-5', NULL, NULL, TRUE, NULL), -- jeszcze nie obsłużone, dlatego naprawy nie ma
  (1, 'fail-2', 'Zła konfiguracja SSH', 'Konfiguracja', '2017-1-1', '2017-1-1', '2017-1-1', TRUE, 50),
  (2, 'fail-3', 'Spalona jednostka zasilania', 'Sprzęt', '2017-12-5', '2017-12-6', NULL, FALSE, 500),
  (3, 'fail-4', 'Luka w zabezpieczeniach systemu - akutalizacja', 'Oprogramowanie', '2017-12-4', '2017-12-5',
   '2017-12-5', TRUE, 40);
