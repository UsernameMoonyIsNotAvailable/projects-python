zero = ['zero','0','zera','zerem']
jeden = ['jeden','1','jedynka','jedynkę']
dwa = ['dwa','2','dwójka','dwója']
trzy = ['trzy','3','trójka','trójkę']
cztery = ['cztery','4','czwórka','czwórkę']
pięć = ['pięć','5','piątka','piątke']
sześć = ['sześć','6','szóstka','szóstkę']
siedem = ['siedem','7','siódemka','siódemkę']
osiem = ['osiem','8','ósemka','ósemkę']
dziewięć = ['dziewięć','9','dziewiątka','dziewiątke']
dziesięć = ['dziesięć','10','dziesiątka','dziesięć']
jedynaście = ['jedynaście','11','jedynastka','jedynastke']
dwanaście = ['dwanaście','12','dwunastka',]
trzynaście = ['trzynaście','13','trzynastka',]
czternaście = ['czternaście','14','czternastka']
piętnaście = ['piętnaście','15','piętnastka',]
szesnaście = ['szesnaście','16','szestnastka']
siedemnaście = ['siedemnaście','17','siedemnastka']
osiemnaście = ['osiembaście','18','osiemnastka']
dziewiętnaście = ['dziewiętnaście','19','dziewięćnastka']
dwadzieścia = ['dwadzieścia','20','dwudziestka']
plus = ['plus','+','dodać','dodaj']
minus = ['minus','-','odejmij','odjąć']
mnożyć = ['mnożyć','*','razy','pomnożyć']
dzielenie = ['podzielić','/','dzielić','dzielone']
baza = [zero,jeden,dwa,trzy,cztery,pięć,sześć,siedem,osiem,dziewięć,dziesięć,jedynaście,dwanaście,trzynaście,czternaście,piętnaście,szesnaście,siedemnaście,osiemnaście,dziewiętnaście,dwadzieścia,plus,minus,mnożyć,dzielenie]

def przetulmacz(slowo):
    for symbol in baza:
        for slowo_symbolu in symbol:
            if slowo == slowo_symbolu:
                return symbol[1]
    return ''

def oblicz(liczba1,liczba2,operacja):
    if operacja == '+':
        return liczba1 + liczba2
    if operacja == '-':
        return liczba1 - liczba2
    if operacja == '*':
        return liczba1 * liczba2
    if operacja == '/':
        return liczba1 / liczba2

def oblicz_z_tekstu(tekst):
    wynik = 0
    liczba = ''
    operacja = ''


    for znak in tekst:
        if znak.isdigit():
            liczba += znak
        else:
            if operacja == '':
                wynik = int(liczba)
            else:
                wynik = oblicz(wynik,int(liczba),operacja)
            liczba = ''
            operacja = znak


    wynik = oblicz(wynik,int(liczba),operacja)
    return wynik

kontynuacja = ''
while kontynuacja != 'n':
    dzialanie = ''
    tekst = input('Podaj dzialanie: ')

    for slowo in tekst.split(' '):
        dzialanie += przetulmacz(slowo)

    print(f'{dzialanie } = {oblicz_z_tekstu(dzialanie)}')
    print('--------------------------------')
    kontynuacja = input('Czy chcesz kontynuowac dzialanie programu? (t/n): ')
print('Koniec!')

