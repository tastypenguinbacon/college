/*
 * Adrian Jałoszewski
 * jaloszewski.adrian@gmail.com
 */

/*
 * Tworzy schemat do zarządzania infrastruktury telekomunikacyjnej
 */
CREATE SCHEMA infrastruktura_telekomunikacyjna;

/*
 * Tabela przechowująca miasta oraz kraje w których się znajdują
 */
CREATE TABLE infrastruktura_telekomunikacyjna.miasto (
  ID    INTEGER PRIMARY KEY,
  KRAJ  VARCHAR(32) NOT NULL,
  NAZWA VARCHAR(64) NOT NULL
);


/*
 * Tabela przechowuje miejsce pracy, zależne od miasta w którym się znajduje,
 * w przypadku zmiany w mieście jest na to przyzwolenie, w przypadku wycofania
 * się z miasta (usunięcie go) miejsce pracy jest usuwane.
 */
CREATE TABLE infrastruktura_telekomunikacyjna.miejsce_pracy (
  id        INTEGER PRIMARY KEY,
  id_miasta INTEGER REFERENCES INFRASTRUKTURA_TELEKOMUNIKACYJNA.MIASTO ON DELETE CASCADE ON UPDATE CASCADE,
  nazwa     VARCHAR(64)  NOT NULL,
  adres     VARCHAR(128) NOT NULL
);

/*
 * Tabela przechowująca dane pracowników. Pracownik może pracować w jednym miejscu
 * pracy. Zmiany w tabeli miejsc pracy są zezwolone, w przypadku usunięcia miejsca
 * pracy pracownik traci pracę (jest usuwany).
 */
CREATE TABLE infrastruktura_telekomunikacyjna.pracownik (
  id               INTEGER PRIMARY KEY,
  id_miejsca_pracy INTEGER REFERENCES INFRASTRUKTURA_TELEKOMUNIKACYJNA.MIEJSCE_PRACY ON DELETE CASCADE ON UPDATE CASCADE,
  imie             VARCHAR(32) NOT NULL,
  nazwisko         VARCHAR(32) NOT NULL,
  email            VARCHAR(64)
);

/*
 * Tabela przechowująca dane producentów sprzętu
 */
CREATE TABLE infrastruktura_telekomunikacyjna.producent (
  id                 INTEGER PRIMARY KEY,
  nazwa              VARCHAR(128) NOT NULL,
  email              VARCHAR(64)  NOT NULL,
  strona_internetowa VARCHAR(64)  NOT NULL
);

/*
 * Tabela przechowująca dane produktów. Zakazane jest usunięcie producenta przed
 * usunięciem wszystkich jego produktów z zarządzania.
 */
CREATE TABLE infrastruktura_telekomunikacyjna.produkt (
  id            INTEGER PRIMARY KEY,
  id_producenta INTEGER REFERENCES infrastruktura_telekomunikacyjna.producent ON DELETE RESTRICT ON UPDATE CASCADE,
  nazwa         VARCHAR(128) NOT NULL,
  typ           VARCHAR(128) NOT NULL
);

/*
 * Tabela przechowująca dane urządzeń. Zakazane jest usunięcie produktu
 * z bazy danych przed usunięciem wszystkich urządzeń jego typu. Tabela
 * posiada unikalny identyfikator wewnętrzny używany w kooperacji z innymi
 * systemami zarządzania
 */
CREATE TABLE infrastruktura_telekomunikacyjna.urzadzenie (
  id                       INTEGER PRIMARY KEY,
  id_produktu              INTEGER REFERENCES infrastruktura_telekomunikacyjna.produkt ON DELETE RESTRICT ON UPDATE CASCADE,
  id_miasta                INTEGER REFERENCES infrastruktura_telekomunikacyjna.miasto ON DELETE RESTRICT ON UPDATE CASCADE,
  identyfikator_wewnetrzny VARCHAR(16) UNIQUE NOT NULL
);

/*
 * Tabela przechowująca informacje na temat metryk
 */
CREATE TABLE infrastruktura_telekomunikacyjna.metryka (
  id        INTEGER PRIMARY KEY,
  jednostka VARCHAR(32),
  nazwa     VARCHAR(32)
);


/*
 * Tabela przechowująca wartości jakie przyjmuje dana metryka w danym czasie.
 * W przypadku usunięcia urządzenia z bazy danych lub usunięcia danego rodzaju
 * metryki tracone są również zebrane wartości.
 */
CREATE TABLE infrastruktura_telekomunikacyjna.wartosc_metryki (
  id            INTEGER PRIMARY KEY,
  id_metryki    INTEGER REFERENCES infrastruktura_telekomunikacyjna.metryka ON DELETE CASCADE ON UPDATE CASCADE,
  id_urzadzenia INTEGER REFERENCES infrastruktura_telekomunikacyjna.urzadzenie ON DELETE CASCADE ON UPDATE CASCADE,
  data_zebrania TIMESTAMP NOT NULL,
  wartosc       DECIMAL   NOT NULL
);

/*
 * Tabela przechowująca informacje na temat awarii. Zawiera informację na temat
 * daty zakończenia awarii, przyczyny, która może przyjmować trzy wartości oraz
 * rozszerzony opis problemu.
 */
CREATE TABLE infrastruktura_telekomunikacyjna.awaria (
  id                       INTEGER PRIMARY KEY,
  identyfikator            VARCHAR(32) UNIQUE NOT NULL, -- identyfikator na potrzeby innych systemów (musi być unikalny)
  opis                     VARCHAR(512), -- nie da się opisać problemu przed
  przyczyna                VARCHAR(16) CHECK (przyczyna IN ('Sprzęt', 'Oprogramowanie', 'Konfiguracja')),
  data_awarii              DATE               NOT NULL,
  data_rozpoczecia_naprawy DATE, -- naprawa awarii może się nie zacząć od raz upo wykryciu
  data_zakonczenia_naprawy DATE, -- awaria może jeszcze nie być naprawiona, dlatego nie ma sprawdzania czy null
  serwisowanie_na_miejscu  BOOLEAN, -- nie da się stwierdzić czy
  koszt                    INTEGER
    CHECK (COALESCE(koszt, 0) >= 0), -- koszt nie może być ujemny może być niewiadomy do końca naprawy
  CONSTRAINT pola_ustawione_po_naprawie -- po naprawie muszą być ustawione wszystkie pola
  CHECK (data_zakonczenia_naprawy IS NULL OR
         (opis IS NOT NULL AND przyczyna IS NOT NULL AND serwisowanie_na_miejscu IS NOT NULL AND koszt IS NOT NULL)),

  CONSTRAINT zakonczenie_jest_po_rozpoczeciu
  CHECK (NOT (data_rozpoczecia_naprawy IS NULL AND data_zakonczenia_naprawy IS NOT NULL) AND
         -- ustawione zakończenie przed ustawieniem rozpoczęcia
         (data_zakonczenia_naprawy IS NULL OR -- obydwa parametry nieustawione
          data_rozpoczecia_naprawy IS NULL OR
          (data_zakonczenia_naprawy <= data_rozpoczecia_naprawy AND
           data_awarii <= data_rozpoczecia_naprawy))) -- warunek kolejności
);