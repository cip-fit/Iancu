"""
Cel mai vizionat film - Fight Club in cazul de mai sus

Utilizatorul cu cele mai multe filme vizionate - Cristian in cazul de mai sus

Extra
Top filme dupa vizionari: Fight Club, Bond, Dracula, Shrek, The nun ...

Top utilizatori cu cele mai multe filme vizionate - Cristian, George, Stefan
"""

x = [
    {'nume': 'George', 'filme': ['Fight Club', 'Shrek', 'Bond']},
    {'nume': 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
    {'nume': 'Stefan', 'filme': ['Fight Club', 'Slumdog Milionaire']}
]

# Combine all films into one list
lista = x[0]['filme'] + x[1]['filme'] + x[2]['filme']

# Loop through the films in lista
while lista: # Cat timp lista nu este goala
    film = lista[0]  # Take the first film
    count = 0

    # Count how many times the film appears
    for f in lista:
        if f == film:
            count += 1

    print(f"{film}: {count}")

    # Remove all occurrences of the film
    while film in lista:
        lista.remove(film)

nr_filme = 0

for i in x:
    if len(i['filme']) > nr_filme:

        nr_filme = len(i['filme'])

        cmmfv = i['nume']

print(f"Utilizatorul cu cele mai multe filme vizionate este {cmmfv} cu {nr_filme} filme.")


#
# counter = {}
#
# for i in x:
#     for j in i['filme']:
#         if j in counter:
#             counter[i] += 1
#         else:
#             counter[i] = 1
#
# sorted_f = []
# for j, count in counter.items():
#     sorted_f.append((j, count))