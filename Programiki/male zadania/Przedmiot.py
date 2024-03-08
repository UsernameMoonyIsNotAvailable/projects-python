class Przedmiot():
    srednia =  0   


    def stworz_liste(self):
        self.oceny = []
        srednia = sum(self.oceny) / len(self.oceny)
        return srednia


    def dodaj_ocene(self,oceny):
        for ocena in oceny:
            self.oceny.append(ocena)

    def wyswietl_oceny(self):
        return self.oceny

    def wyswietl_srednia(self):
        print(self.srednia)

    





    
