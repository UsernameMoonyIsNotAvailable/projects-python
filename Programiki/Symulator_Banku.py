 #Bank
#Funkcje do pokazywania wyboru opcji
def menu():
    print('Ktora opcje wybierasz?')
    print('1.Wplata')
    print('2.Wyplata')
    print('3.Sprawdz stan konta')
    print('4.Wyjdz')
#Funckaj pytająca o twój wybór
def wybor_opcji():
    print()
    return int(input('Ktora opcje wybierasz? Wpisz numer tej opcji. '))
#Funkcja do Wypłaty i Wpłaty    
def pobieranie_kwoty(kwota):
    return float(input(kwota))

def stan_konta(saldo):
    print(f'stan konta wynosi {saldo}zł')
    print()
#funkcja do wpłacania
def wplacanie(saldo):
    print()
    kwota_wplaty = pobieranie_kwoty('Ile chcesz zl wpłacić? ')
    saldo = saldo + kwota_wplaty
    stan_konta(saldo)
    return saldo
#Funkcja do wypłacania
def wyplacanie(saldo):
    kwota_wyplaty = pobieranie_kwoty('Ile chcesz wypłacić? ')
    if kwota_wyplaty > saldo:
        print('Wypłata nieudana, za mało środków na koncie')
    else:
        saldo -= kwota_wyplaty
        stan_konta(saldo)  # Wyświetl aktualny stan konta
    return saldo


wybor = 0
saldo = 0



#Obsługiwanie wyborów

while wybor != 4:
        menu()
        wybor = wybor_opcji()
        if wybor == 1:
            saldo = wplacanie(saldo)
        elif wybor == 2:
            saldo = wyplacanie(saldo)
            continue
        elif wybor == 3:
            saldo = stan_konta(saldo)
        elif wybor == 4:
            print('Kończenie programu')
            break
        else:
            print('Nie poprawny wybór! ')
