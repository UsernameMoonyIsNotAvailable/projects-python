
liczby = [1, 2, 3, 4, 5, 6]
def parzyste(liczby):
    liczby_parzyste = []
    for i in liczby:
        if i % 2 == 0:
            liczby_parzyste.append(i)
    return sum(liczby_parzyste)

print(parzyste(liczby))



