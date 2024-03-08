for liczba in range(1,101):
    if liczba % 3 == 0 and liczba % 5 == 0:
        print('fizzbuzz')
    elif liczba % 3 == 0:
        print('fizz')
    elif liczba % 5 == 0:
        print('buzz')
    else:
        print(liczba)
    
