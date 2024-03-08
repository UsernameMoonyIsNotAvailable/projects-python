
liczby = [9, 10, 12, 15, 20, 25]
def parzyste(liczby):
    liczby_nieparzysgte = []
    for i in liczby:
        if i % 2 != 0 and i > 10:
            liczby_nieparzysgte.append(i)
    return liczby_nieparzysgte
    

print(parzyste(liczby))
