# Combina toate filmele intr-o lista


"""
[ {
   'nume': 'George',
   'filme': ['Shrek', 'Bond', 'Fight Club']
 },
{
 'nume' : 'Cristian',
 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']
},
{
 'nume' : 'Stefan',
 'filme': ['Fight Club', 'Slumdog Milionare']
}
]

Avand o lista de utilizatori si filme vizionate, listati:

1️⃣ Cel mai vizionat film - Fight Club in cazul de mai sus
    ✅ Creeaza o lista cu toate filmele
❌ Utilizatorul cu cele mai multe filme vizionate - Cristian in cazul de mai sus

Extra
Top filme dupa vizionari: Fight Club, Bond, Dracula, Shrek, The nun ...
Top utilizatori cu cele mai multe filme vizionate - Cristian, George, Stefan
"""

lista_filme = [ {
   'nume': 'George',
   'filme': ['Shrek', 'Bond', 'Fight Club']
 },
{
 'nume' : 'Cristian',
 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']
},
{
 'nume' : 'Stefan',
 'filme': ['Fight Club', 'Slumdog Milionare']
} ]

# cmvf = ()

# toate_filmele = []
#
# for i in lista_filme:
#     for j in i['filme']:
#         toate_filmele.append(j)
# print(toate_filmele)

toate_filmele = lista_filme[0]['filme'] + lista_filme[1]['filme'] + lista_filme[2]['filme']

print(toate_filmele)

a = len(toate_filmele)
# print(a)

max_count = 0

for i in range(a):
    count = 0

    for j in range(a):

        if toate_filmele[i] == toate_filmele[j]:
            count += 1
        if count > max_count:
            max_count = count
            cmvf = toate_filmele[i]

print(cmvf)
