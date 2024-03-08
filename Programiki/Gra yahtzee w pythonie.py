import random
kosci = [1,2,3,4,5]
nazwy_punktow = ['Jedynki','Dwójki','Trójki','Czwórki','Piątki','Szóstki','3 jednakowe','4 jednakowe']
punkty = ['','','','','','','','']

def rzuc_koscmi(numery_kosci:str):
    for i in numery_kosci:
        index = int(i) - 1
        kosci[index] = random.randint(1,6)


def pokaz_kosci():
    print('_____________________________')
    for i in range(len(kosci)):
        print(f'{i+1}. {kosci[i]}')
    print('_____________________________')

def sprawdz_czy_przerzucamy():
    odp = input('Czy chcesz przerzucać kośći?(t/n) '  )
    if odp == 't':
        return True
    return False

def wstaw_3i4_jednakowe(pole,ilosc):
    lista_wystapien = [0,0,0,0,0,0]
    for kosc in kosci:
        lista_wystapien[kosc-1] += 1
    if ilosc in lista_wystapien:
        punkty[pole-1] = sum(kosci)
    else:
        punkty[pole-1] = 0




def pokaz_tabele_punktow():
    print('_____________________________')
    for i in range(len(punkty)):
        print(f'{i+1}.{nazwy_punktow[i]}\t{punkty[i]}')
    print('_____________________________')

def wstaw_w_liczbowym(liczba):
    liczba_punktow = 0
    for kosc in kosci:
        if kosc == liczba:
            liczba_punktow += kosc
    punkty[liczba-1] = liczba_punktow

def wstaw_punkty():
    pole = int(input('Gdzie chcesz wstawić punkty (podaj numer rubryki): '))
    if punkty[pole-1] == '':
        if 1 <= pole <= 6:
            wstaw_w_liczbowym(pole)
        elif pole == 7:
            wstaw_3i4_jednakowe(pole,3)
        elif pole == 8:
            wstaw_3i4_jednakowe(pole, 4)
        else:
            print('Wybrałeś pole w którym już wstawiłeś punkty')
            wstaw_punkty()

rzuc_koscmi('12345')
pokaz_tabele_punktow()
pokaz_kosci

for tura in range(len(punkty)):
    rzuc_koscmi('12345')
    pokaz_tabele_punktow()
    pokaz_kosci()

    for i in range(2):
        czy_przerzut = sprawdz_czy_przerzucamy()
        if czy_przerzut:
            kosci_do_przerzutu = input('Wypisz numery kości,które chcesz przerzucić(bez spacji): ')
            rzuc_koscmi(kosci_do_przerzutu)
            pokaz_kosci()
        else:
            break

    pokaz_tabele_punktow()
    pokaz_kosci()
    wstaw_punkty()
    pokaz_tabele_punktow()
print(f'Twój wynik to: {sum(punkty)}')
