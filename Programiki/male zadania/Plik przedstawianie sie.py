from uzytkownik import Uzytkownik
user1 = Uzytkownik()
user2 = Uzytkownik()
user3 = Uzytkownik()
user4 = Uzytkownik()

user1.imie = 'Jan'
user1.nazwisko = 'Kowalski'
user1.wiek = 32

user2.imie = 'Grzegoz'
user2.nazwisko = 'Brzeczyszczykiewicz'
user2.wiek = 21

user3.imie = 'Marek'
user3.nazwisko = 'Bozik'
user3.wiek = 33

user4.imie = 'Jartek'
user4.nazwisko = 'Barkiewicz'
user4.wiek = 16

user1.zmien_wiek(14)

user1.przedstaw_sie()
user2.przedstaw_sie()
user3.przedstaw_sie()
user4.przedstaw_sie()

