#Password prompt

q=''

while q != 'secret123':
    q = input('Parola: ')
    if q == 'secret123':
        print('Parola corecta.')
        break
    else:
        print('Parola este gresita.')