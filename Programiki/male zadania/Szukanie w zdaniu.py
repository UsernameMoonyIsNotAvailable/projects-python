import re

def slowa_na_A(a):
    slowa = r'\b[Aa]\w+' 
    funkcja = re.findall(slowa, a)
    return funkcja

print(slowa_na_A('Ameryka,banan,amelka,Ania,helikotper'))