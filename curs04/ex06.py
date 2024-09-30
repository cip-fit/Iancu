# Scrieti un program care sa faca split dupa al n-lea element intr-o lista:

# lista_1 = []
# lista_2 = []
# lista_3 = []

lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
result = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

a = len(lista_start)

lista_n = []

for i in range(n):

    lista_micuta = []

    for j in range(a):  # range(x) este de la 0 la x-1 !!! nu il include pe x

        if j % n - i == 0:
            lista_micuta.append(lista_start[j])

    lista_n.append(lista_micuta)

print(lista_n)

# if i % n-1 == 0:
#     lista_2.append(lista_start[i])
#
# if i % n-2 == 0:
#     lista_3.append(lista_start[i])

# print(lista_1, lista_2, lista_3)
