"""
Cel mai vizionat film - Fight Club in cazul de mai sus

Utilizatorul cu cele mai multe filme vizionate - Cristian in cazul de mai sus

Extra
Top filme dupa vizionari: Fight Club, Bond, Dracula, Shrek, The nun ...

Top utilizatori cu cele mai multe filme vizionate - Cristian, George, Stefan
"""

x = [
    {'nume': 'George',
     'filme': ['Shrek', 'Bond', 'Fight Club']},
    {'nume': 'Cristian',
     'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
    {'nume': 'Stefan',
     'filme': ['Fight Club', 'Slumdog Milionaire']}
]


# Lista nr filme

filme = []

for i in x:
    for film in i['filme']:
        filme.append(film)
print(filme)

a = len(filme)

max_count = 0

for i in range(a):

    count = 0

    for j in range(a):

        if filme[i] == filme[j]:
            count += 1

    if count > max_count:
        max_count = count
        cmvf = filme[i]

print(cmvf)





filme_vazute = 0

# Pentru prima pozitie, i preia valuarea primului dictionar din lista

for i in x:

    if len(i['filme']) > filme_vazute:

        filme_vazute = len(i['filme'])
        cmmfv = i['nume']

print(cmmfv)

"""
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

a = sorted(lista)
print(a)

# Length of the list to determine how many times to loop
a = len(lista)

# OL: Allows us to access 0 to n-1 / i becomes 0, 1, 2, 3
for i in range(a):

# IL: Starts from i+1 up to end of the list
    for j in range(i + 1, a):

# Compare first element with the second
        if lista[i] < lista[j]:

# For i=0, j=1: list[i] = 7, list[j] = 8
            lista[i], lista[j] = lista[j], lista[i]

# Print list in a descending order
print(lista)

"""

# Frecventa filmelor
movie_counts = {}

for i in filme:
    if i in movie_counts:
        movie_counts[i] += 1
    else:
        movie_counts[i] = 1
print(movie_counts)

# Top filme
top_filme = list(movie_counts.items())

# print(lista_filme)

for i in range(len(top_filme)):

    for j in range(i+1, len(top_filme)):

        if top_filme[i][1] < top_filme[j][1]:

            top_filme[i], top_filme[j] = top_filme[j], top_filme[i]
for i, v in top_filme:
    print(i + " a fost vizionat de " + str(v) + " ori.")

# Top cinefili

cinefili = []
for i in x:

    nume = i['nume']
    filme_vazute = len(i['filme'])
    cinefili.append((nume, filme_vazute))

for i in range(len(cinefili)):
    for j in range(i + 1, len(cinefili)):
        if cinefili[i][1] < cinefili[j][1]:

            cinefili[i], cinefili[j] = cinefili[j], cinefili[i]

for i, v in cinefili:
    print(i + ": " + str(v) + " filme")