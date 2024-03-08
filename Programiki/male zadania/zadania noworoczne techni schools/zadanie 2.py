def czy_mozna_zbudowac_trojkat(bok1,bok2,bok3):
    return bok1 + bok2 > bok3 and bok1 + bok3 > bok2 and bok2 + bok3 > bok1


bok_pierwszy = float(input('Podaj dlugosc pierwszego boku: '))
bok_drugi = float(input('Podaj dlugosc pierwszego drugiego: '))
bok_trzeci = float(input('Podaj dlugosc pierwszego trzeciego: '))

if czy_mozna_zbudowac_trojkat(bok_pierwszy,bok_drugi,bok_trzeci):
    print('Da sie utworzyc trojkont z podanych bokow.')
else:
    print('Nie da sie utworzyc trojkonta z takich bokow')
