class Kalkulator:
    def __init__(self, wynik_poczatkowy=0):
        self.wynik = wynik_poczatkowy
    
    def dodawanie(self,x):
        self.wynik += x
        print(self.wynik)

    def odejmowanie(self,x):
        self.wynik -= x
        print(self.wynik)

    def mnozenie(self,x):
        self.wynik *= x
        print(self.wynik)

    
    def dzielenie(self,x):
        if x != 0:
            self.wynik /= x
        else:
            print('Nie można dzielić przez zero!')


kalk = Kalkulator()

while True:
    print(f'1. Dodaj\n2. Odejmij\n3. Pomnóż\n4. Podziel\n5. Zakończ program\nAktualny wynik to {kalk.wynik}')

    opcja = int(input('Wybierz opcje od 1-5: '))

    if opcja == 1:
        x = float(input('Podaj liczbę którą chcesz dodać: '))
        kalk.dodawanie(x)
    elif opcja == 2:
        x = float(input('Podaj liczbę którą chcesz odjąć: '))
        kalk.odejmowanie(x)
    elif opcja == 3:
        x = float(input('Podaj liczbe do pomnożenia: '))
        kalk.mnozenie(x)
    elif opcja == 4:
        x = float(input('Podaj liczbe do podzielenia: '))
        kalk.dzielenie(x)
    elif opcja == 5:
        print('Progam zakończony')
        break
    else:
        print('Nie poprawna opcja')


    