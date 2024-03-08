class Pojazd():
    marka = ''
    rok = 0
    typ = ''


    def wyswietl(self):
        print(self.marka)
        print(self.rok)
        print(self.typ)



auto = Pojazd()
auto.marka = 'Honda Civic'
auto.rok = 2006
auto.typ = 'Żywy'

auto2 = Pojazd()
auto2.marka = 'Honda Civic2'
auto2.rok = 2002
auto2.typ = 'Żywy2'


auto.wyswietl()

auto2.wyswietl()