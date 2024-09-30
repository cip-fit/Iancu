"""
Se citeste un numar intreg de la tastatura

Daca numarul este divizibil cu:

3 - se afiseaza Fizz
5 - se afiseaza Buzz
3 si 5 - se afiseaza FizzBuzz
In caz contrar se afiseaza numarul citit
"""

while True:

    x = int(input('Alege un numar: '))
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
        break
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fizz')
    else:
        print('Mai incearca odata')