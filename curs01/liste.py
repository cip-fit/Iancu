"""
lista = []
    ordonata
    putem avea valori duplicate
    sunt structuri de date ale caror elemente pot fi accesate cu index
        index incepe cu 0 de la cap, -1 de la coada

"""

lista = [8, 2, 8 , 'Ana are mere', 4.2, True]
# print(lista[6])

"""
    functia slice = taie elementele in functie de primul element inclus pana la ultimul element
    functia len = cate elemente sunt in respectiva lista
"""

# print(lista[4:6])
# print(lista[2:8]) #avantaj slice: putem extrage toate lementele dintr-o lista daca punem un numar mai mare decat numarul de elemente dintr-o lista, exemplu aici 8

# print(lista[-6:]) #aici, slice v-a afisa toata lista de la stanga la dreapta, mereu v-a contoriza in functie de aceasta regula

# print(lista[2:8:2]) #aici, incepand cu element nr 2, pana la element nr 8, cu pas 2

lista.append(5.6)
# print(lista.index(8)) #aici, afisam index-ul
#
# lista.remove(2)
# print(lista)
#
lista.pop(3)
# print(lista)
#
# lista.clear()

# lista.reverse()
# print(lista)

lista.sort() #sort nu are cum sa sorteze string-uri
print(lista)

print(type(lista))

