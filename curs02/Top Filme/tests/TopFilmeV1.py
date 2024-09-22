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

a = x[0]['filme']
set_a = set(a)
b = x[1]['filme']
set_b = set(b)
c = x[2]['filme']
set_c = set(c)

d = set()
d = set_a.intersection(set_b).intersection(set_c)
print(f'Cel mai vizionat film este {d}')

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