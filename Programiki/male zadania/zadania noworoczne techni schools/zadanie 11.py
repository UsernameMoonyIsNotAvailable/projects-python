#główna funkcja
def sprawdzanie(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return False
#wagi,sumy,cyfry kontrolne    
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = sum(int(pesel[i]) * wagi[i] for i in range(10))
    kontrolna = (10 - suma % 10) % 10
#zwracanie    
    return kontrolna == int(pesel[10])
#Wpisywanie swojego pesela

def pesel_input():
    pesel = input('Podaj numer PESEL: ')
    if sprawdzanie(pesel):
        print('PESEL jest poprawny')
    else:
        print('Zły kod PESEL!')
#czy program główny
if __name__ == "__main__":
    pesel_input()