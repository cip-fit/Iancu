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
filme = x[0]['filme'] + x[1]['filme'] + x[2]['filme']
print(filme)

a = len(filme)
print(a)
b = 0

for i in range(a):
    for j in range(a):
        if filme[i] == filme [j]:
            b += 1
print(b)