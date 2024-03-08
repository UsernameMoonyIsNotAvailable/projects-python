

def palindrodim(slowo):
    slowo = slowo.lower()
    if slowo == slowo[::-1]:
        return slowo
    else:
        print('Twoje slowo nie jest palindromem')

print(palindrodim('tacocat'))