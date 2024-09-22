import random

# Cuvantul de ghicit
word = input('Cuvantul de ghicit este: ')
word_length = len(word)

# Cate indicii se vor arata
nr_i = 2

# Pozitiile indicilor
pozitii_i = random.sample(range(1, word_length - 1), nr_i)

# Cuvantul listat cu underscore
h_word = ['_'] * word_length

# Prima si ultima litera
# h_word[0] = word[0]
# h_word[-1] = word[-1]

# Arata indiciile in mod aleatoriu
for i in pozitii_i:
    h_word[i] = word[i]

# Convertim lista inapoi in string
h_word = ''.join(h_word)

# Print cuvantul ascuns
print('\n'*20, h_word)

lives = 7

while word != h_word and lives > 0:

    litera = input('Alege o litera: ')
    lista_h_word = list(h_word)

    if litera in word:

        for i in range(word_length):

            if litera == word[i]:
                lista_h_word[i] = litera

        h_word=''.join(lista_h_word)
        print(h_word)

    else:
        lives -= 1
        if lives != 0:
            print(f'Mai ai {lives} vieti')

if h_word == word:
    print(f'Felicitari! Cuvantul este: {h_word}')
else:
    print(f'Ai pierdut! Cuvantul era: {word}')