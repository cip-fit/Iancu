"""

scrieti un program care sa extraga inversul dintr-un nr.

Exemplu: 7536 trebuie afisati 6 3 5 7

"""

n = input('n: ')
invers = str()

for i in n:

    invers = i + invers

print(invers)