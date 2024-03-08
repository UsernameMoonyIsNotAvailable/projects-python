import math
def dodawanie (a, b):
    return a + b
def odejmowanie (a, b):
    return a - b
def mnozenie (a, b):
    return a * b
def potegowanie (a, b):
    return a ** b
def modulo (a, b):
    return a % b
def logarytm (a, b):
    return math.log(a)
def logarytm2 (a, b):
    return math.log(a,b)
def pierwiastkowanie (a, b):
    return a ** 0.5
def sin (a):
    return math.sin(a)
def dzielenie (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Nie dziel przez zero!'
    
while True:
    print('Wybierz dzialanie:')
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("6. Reszta z dzielenia")
    print("7. Pierwiastkowanie")
    print("8. Logarytym o podstawie 10")
    print("9. Logarytym o podstawie 2 liczby")
    print("10.Wyrażenie trygonometryczne sin (na 1 liczbe)")
    wybor = input('Wybierz opcje 1-10 ')
    a = int(input('Wprowadz pierwsza liczbe:  '))
    b =int(input('Wprowadz druga liczbe:  '))
    
    if wybor == '1':
        wynik = dodawanie(a, b)
    elif wybor == '2':
        wynik = odejmowanie(a, b)
    elif wybor == '3':
        wynik = mnozenie(a, b)
    elif wybor == '4':
        wynik = dzielenie(a, b)
    elif wybor == '5':
        wynik = potegowanie(a, b)
    elif wybor == '6':
        wynik = modulo(a, b)
    elif wybor == '7':    
        wynik = pierwiastkowanie(a, b)
    elif wybor == '8':
        wynik = int(logarytm(a, b))
    elif wybor == '9':
        wynik = int(logarytm2(a, b))
    elif wybor == '10':
        wynik = int(sin(a,b))
    else:
        print('Nie wlasciwy wybor!')
    print(wynik)
    c =  input('chcesz kontynuowac? jezeli tak,to prosze wpisac tak:  ')
    if c == 'tak':
        continue
    else:
        break   
