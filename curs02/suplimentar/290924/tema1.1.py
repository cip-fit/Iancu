"""1. Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de

caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.

In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de

caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru

preluat automat de la tastatura.
"""

text = input('Numele: ')
is_string = False

for i in text:

    if i not in ('0123456789'):
        is_string = True
        break

if is_string is True:
    print(f'Sirul de caractere a fost gasit de {text}')
else:
    print('Este de fapt un numar')