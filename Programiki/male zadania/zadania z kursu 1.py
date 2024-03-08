# liczba = int(input('Podaj liczbe: '))
# for i in range(liczba + 1):
#     for i in range(liczba):
#         print(i,end='')
#     print()
# ------------------------------------------------------
# lista_liczy = [1,2,3,4,5]
# lista_liczy.sort()
# print(f'najwiekszy element w liscie to {lista_liczy[-1]} a najmniejszy to {min(lista_liczy)}')




# lista_nowa = [1,2,3,4,5,67,37]
# def lista_sortowanie(lista_nowa):
#     for i in lista_nowa:
#         lista_nowa.sort()
#         i = min(lista_nowa)
#         return i

# print(f'najwienkszy {lista_nowa[-1]} a najmniejszy {lista_sortowanie(lista_nowa)}')
    
text = 'ABC przykladowy tekst na potrzeby naszego programu'
litery = 0
slowink = {}
def slowa_w_tekscie(text):
    a = len(text.split(' '))
    return a

def ile_liter(text):
    lista = []
    for i in text:
        if i == ' ':
            continue
        else:
            lista.append(i)
    return len(lista)



print(f'Ilosc slow wynosi:{slowa_w_tekscie(text)}')
print(f'Ilosc liter wynosi:{ile_liter(text)}')



