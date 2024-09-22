#Greater Number

print('Alege doua numere!')

a = int
b = int

while a != 0 and b != 0:

    a = int(input('A: '))
    b = int(input('B: '))

    if a > b:
        print('A > B')
        break
    elif a < b:
        print('A < B')
        break
    if a == b:
        print('Alege alte numere')
