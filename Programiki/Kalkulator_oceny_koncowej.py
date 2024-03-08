# Funkcje:
# Wprowadzanie ocen z różnych kategorii (np. testy, prace domowe, aktywność).
# Możliwość ustalenia wagi dla każdej kategorii.
# Obliczanie średniej ważonej.
# Wizualizacja postępu ucznia.
# Opcjonalnie: Możliwość zapisu i odczytu danych ucznia z pliku.
# Technologie / Tematy:
# Podstawowe operacje wejścia/wyjścia.
# Praca z typami danych, takimi jak listy i słowniki.
# Obsługa błędów.
# Czytanie i zapisywanie danych do pliku.


def wprowadz_oceny():

  oceny = {}

  kategoria = ["Sprawdzian", "Praca domowa", "Aktywnosc", "Kartkowka"]

  for kategoria in kategoria:
    try:
      ocena = float(input(f"Podaj ocenę z {kategoria}: "))
      waga = float(input("Podaj wagę oceny (zakres 0-1): "))
    except ValueError:
      print("Błędny format danych. Podaj liczbę.")
      continue

    if 1 <= ocena <= 6 and 0 <= waga <= 1:
      oceny[kategoria] = {"ocena": ocena, "waga": waga}
    else:
      print(f"Błędna wartość oceny lub wagi dla {kategoria}.")

  return oceny




def obliczenie_srednia(oceny):

  suma_ocen = 0
  for ocena in oceny.values():
    suma_ocen += ocena["ocena"] * ocena["waga"]




  suma_wag = sum(ocena["waga"] for ocena in oceny.values())


  licznik = suma_ocen
  mianownik = suma_wag
  srednia = licznik / mianownik

  return srednia



def wyswietl_srednia(dane_ucznia, srednia_ocen):


  print(f"**Dane ucznia:**")
  for kategoria, dane in dane_ucznia.items():
    print(f"- {kategoria}: ocena: {dane['ocena']}, waga: {dane['waga']}")

  print(f"**Średnia ocen: {srednia_ocen}")

def zapisz_do_pliku(dane_ucznia, srednia_ocen):

  with open("oceny.txt", "w") as plik:
    plik.write(f"**Dane ucznia:**\n")
    for kategoria, dane in dane_ucznia.items():
      plik.write(f"- {kategoria}: ocena: {dane['ocena']}, waga: {dane['waga']}\n")

    plik.write(f"\n**Srednia ocen: {srednia_ocen}")

def odczytaj_plik(nazwa_pliku):

  try:
    with open(nazwa_pliku, "r") as plik:
      zawartosc = plik.read()
    print(zawartosc)
  except FileNotFoundError:
    print(f"Plik {nazwa_pliku} nie istnieje.")


dane_ucznia = wprowadz_oceny()
srednia_ocen = obliczenie_srednia(dane_ucznia)

print(f"Srednia ocen: {srednia_ocen}")


wyswietl_srednia(dane_ucznia, srednia_ocen)
zapisz_do_pliku(dane_ucznia, srednia_ocen)
odczytaj_plik("oceny.txt")
