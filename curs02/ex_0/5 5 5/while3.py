#Number Guesser

nr = 7

while True:
    q = int(input('Numarul secret: '))
    if q == 7:
        print('Raspuns corect')
        break
    else:
        print('Mai incearca')