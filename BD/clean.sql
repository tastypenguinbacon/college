/*
 * Adrian Jałoszewski
 * jaloszewski.adrian@gmail.com
 */

/*
  Usuwanie tabeli awarii
 */
DROP TABLE infrastruktura_telekomunikacyjna.awaria;

/*
  Usuwanie tabel zależnych od metryki
 */
DROP TABLE infrastruktura_telekomunikacyjna.wartosc_metryki;
DROP TABLE infrastruktura_telekomunikacyjna.metryka;

/*
  Usuwanie tabel zależnych od rodzaju sprzętu
 */
DROP TABLE infrastruktura_telekomunikacyjna.urzadzenie;
DROP TABLE infrastruktura_telekomunikacyjna.produkt;
DROP TABLE infrastruktura_telekomunikacyjna.producent;

/*
  Usuwanie tabel zależnych od pracownika
 */
DROP TABLE infrastruktura_telekomunikacyjna.pracownik;
DROP TABLE infrastruktura_telekomunikacyjna.miejsce_pracy;
DROP TABLE infrastruktura_telekomunikacyjna.miasto;

/*
  Usuwanie schematu
 */
DROP SCHEMA INFRASTRUKTURA_TELEKOMUNIKACYJNA;
