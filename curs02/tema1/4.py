"""
4. Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
afisati numarul pozitiv.
"""

nr = int(input('Introduceti un numar: '))

if nr > 0 and nr < 10:
    print(f'Numarul {nr} este mai mic decat 10.')
elif nr == 0:
    print(f'Numarul {nr} este 0')
if nr < 0:
    nr = -nr
    print(f'Numarul {nr} a fost transformat in numar natural.')
