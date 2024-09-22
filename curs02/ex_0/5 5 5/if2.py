#Age Check:

varsta = int(input('Verifica varsta: '))

if varsta >= 18 and varsta < 85:
    print('Sunteti adult')
else:
    if varsta >= 85:
        print('Mai tastati odata')
    elif varsta <4:
        print(' Mai tastati odata')
    else:
        print('Sunteti copil')