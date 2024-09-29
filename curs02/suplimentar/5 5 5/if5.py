# Pw Check
i = 3
q = int

while i > 0:
    q = int(input('Password? '))

    if q == 12345:
        print('Acces')
        break
    else:
        i -= 1
        if i > 0:
            print(f'Rejected. You have {i} more tries.')
        else:
            print("You are out of tries. Access denied.")