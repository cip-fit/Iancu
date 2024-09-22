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

# Create sets for each person's films
set_a = set(x[0]['filme'])
set_b = set(x[1]['filme'])
set_c = set(x[2]['filme'])

# Find the intersection manually
d = set()  # Start with an empty set

for i in set_a:
    if i in set_b and i in set_c:
        d.add(i)

print(f'Cel mai vizionat film este {d}')


nr_filme = 0

for i in x:
    if len(i['filme']) > nr_filme:
        nr_filme = len(i['filme'])
        cmmfv = i['nume']
print(f"Utilizatorul cu cele mai multe filme vizionate este {cmmfv} cu {nr_filme} filme.")


