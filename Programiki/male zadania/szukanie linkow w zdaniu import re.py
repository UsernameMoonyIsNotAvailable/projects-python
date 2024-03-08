import re

def szukanie_linkow(a):
    slowa = r'https?://\S+'
    linki = re.findall(slowa,a)
    return linki


print(szukanie_linkow('Odwiedź http://example.com/ i https://www.example.org/ albo https://wikipedia.org'))
