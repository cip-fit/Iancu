"""

2. Creati un program in care utilizatorul sa introduca un numar. Validati daca acest

numar este par sau impar si afisati un raspuns in acest sens.
"""

nr = int(input('Alege un numar: '))

if nr % 2 == 0:
    print(f'Numarul {nr} este par')
elif nr % 3 == 0:
    print(f'Numarul {nr} este impar')
else:
    print(f'Inputul {nr} nu este numar')
