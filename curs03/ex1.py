numar_telefon = input('nr tel: ')

stringuri = None

if len(numar_telefon) == 12 and numar_telefon[0: 3] == '+40':
    stringuri = False

    for i in numar_telefon[3:13]:
        if i in '0123456789':
            stringuri = True

if stringuri is True:
    print('valid')
else:
    print('invalid')