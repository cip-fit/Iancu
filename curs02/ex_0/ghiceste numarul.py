import random
n1 = random.randint(1, 10)

lives = 3

while lives > 0:
    n2 = int(input('Guess: '))

    if n2 == n1:
        print('Right!')
        break
    elif n2 > n1:
        print('Too high!')
    else:
        print('Too low!')
    lives -= 1

if lives == 0:
    print('You lost! The number was', n1)