"""
se cer 2 nr intregi de la tastatura. sa se calculeze produsul

daca produsul celor 2 nr este mai mic sau egal cu 1000, altfel sa se returneze suma acestora
"""

text1 = input('nr 1')
text2 = input('nr 2')

# produs=()
# suma=()

rez = None
op = None

if text1.isdigit() and text2.isdigit():

    text1=int(text1)
    text2=int(text2)

    if (rez:=text1*text2) and rez <= 1000:
        operatie = 'produs'
    else:
        rezultat = text1 + text2
        operatie = 'suma'

    if operatie == 'produs':
        print(rezultat)

# print(f'Produsul este: {produsul}', f'Suma este: {suma}')