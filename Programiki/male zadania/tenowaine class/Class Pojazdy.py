class Pojazd():
    def __init__(self,marka,rok):
        self.rok = rok
        self.marka = marka
        
    def jazda(self):
        print(f'{self.marka} porusza sie ')

    def czy_elektryczny(self):
        print(f'{self.marka} jest autem elektrycznym')








pojazd1 = Pojazd('Honda Civic',1999)
pojazd1.jazda()
    