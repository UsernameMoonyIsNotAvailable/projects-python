class Samochod():
    def __init__(self,marka,model,moc_km):
        print('Utworzenie obiektu samochod')
        self.marka = marka
        self.model = model
        self.moc_km = moc_km


auto1 = Samochod('Ford','Mustang','320')
'________________________________________________________________'
class Samochod():
    marka = ''
    model = ''
    moc_km = ''

auto1 = Samochod()
auto1.marka = 'ford'
auto1.model = 'mustang'
auto1.moc_km = '320'

auto1.__init__()