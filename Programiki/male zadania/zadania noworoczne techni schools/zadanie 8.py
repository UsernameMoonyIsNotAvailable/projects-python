import random
import string
dlugosc = int(input('Ile znakow ma miec haslo: '))

def generowanie_hasla(dlugosc):
    male_litery = string.ascii_lowercase
    duze_litery = string.ascii_uppercase
    liczby = string.digits
    znaki_specjlane = string.punctuation
    
    haslo = random.choice(male_litery)
    haslo += random.choice(duze_litery)
    haslo += random.choice(liczby)
    haslo += random.choice(znaki_specjlane)

    
    reszta_dlugosci = dlugosc - 4
    haslo += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=reszta_dlugosci))
    

    hasla = list(haslo)
    random.shuffle(hasla)
    haslo = ''.join(hasla)

    return haslo

if dlugosc < 16:
    print('Za krótkie hasło. Silne hasło powinno mieć 16 znaków')
else:
    haslo = generowanie_hasla(dlugosc)
    print(f'Twoje wygenerowane hasło to: {haslo}')


    



