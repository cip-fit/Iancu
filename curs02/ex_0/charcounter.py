
word = 'simplicity' # Cuvantul ales
counter = {} # Declaram counter dictionar

for letter in word: # Pentru fiecare litera in cuvant

    if letter in counter: # Daca litera este in cuvant
        counter[letter] += 1 # Counter[letter] ii pastreaza definitia de dictionar
    else:
        counter[letter] = 1

print(counter)