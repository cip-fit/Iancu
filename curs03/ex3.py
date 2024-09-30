cuvant = input('adauga: ')

vocale = 0
consoane = 0

for i in cuvant:
    if i in 'aeiou':
        vocale +=1
    else:
        consoane += 1
print(f'nr vocale este {vocale} si consoane {consoane}')