class Uzytkownik():
    imie = ''
    nazwisko = ''
    wiek = 0


    def przedstaw_sie(self):
        print(self.imie,self.nazwisko)
        if self.wiek >= 18:
            print(f'{self.imie} ma {self.wiek} lat,jest pełnoletni')
        else:
            print(f'{self.imie} ma {self.wiek} lat,jest niepełnoletni')

    def zmien_wiek(self, nowy_wiek):
        self.wiek = nowy_wiek
        
