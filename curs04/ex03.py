"""

problema in problema

Scrieti suma cu iteratie prin aceasta

"""

lista = [10, 13, 2, 6, 14]
suma = None


for i, element in enumerate(lista):

    print(i, element)

    if i != len(lista)-1:

        suma = element + lista[i+1]
        print(suma)