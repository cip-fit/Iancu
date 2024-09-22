"""
3. Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este

bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact

la 4 (fara rest)
"""

an = int(input('Introduceti un an: '))

if an % 4 == 0:
    print(f'Anul {an} este bisect.')
else:
    print(f'Anul {an} nu este bisect.')