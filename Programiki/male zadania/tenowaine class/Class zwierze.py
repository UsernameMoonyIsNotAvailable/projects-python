class Zwierze():
    def __init__(self, wiek, imie):
        self.wiek = wiek
        self.imie = imie

    def wydajDzwiek(self):
        print(f'{self.imie} wydaje dzwięk')

    def jedz(self):
        print(f'{self.imie} je')

class Ptak(Zwierze):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)

    def latanie(self):
        print(f'{self.imie} lata')



class Kot(Zwierze):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)
    
    def drapanie(self):
        print(f'{self.imie} drapie')


class Orzel(Ptak):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)

    def poluj(self):
        self.latanie()
        print(f'{self.imie} poluje')


class Pies(Zwierze):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)
        self.rasa = 'mops'

    def wypiszrase(self):
        print(f'{self.imie} jest rasy: {self.rasa}')


zwierze1 = Zwierze(112,'Sznoizer')
zwierze1.wydajDzwiek()
zwierze1.jedz()
print('_______________')
pies1 = Pies(8, 'Neil')
pies1.wydajDzwiek()
pies1.jedz()
print('_______________')
kot1 = Kot(10, 'Marek')
kot1.wydajDzwiek()
kot1.jedz()
kot1.drapanie()
print('_______________')
ptak1 = Ptak(21,'Equador')
ptak1.wydajDzwiek()
ptak1.jedz()
print('_______________')
orze1 = Orzel(5,'Orzelek')
orze1.poluj()
orze1.wydajDzwiek()


