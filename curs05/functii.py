"""
O functie are un singur scop. Cu atat este mai mult la obiect, cu atat este mai refolosibila.
-> functii mici si mobile
"""

# print("Ana") #functia 'print' cu parametrii in paranteza
#
# input()


# def functia_mea(param_1, param_2):
#     return "Ana are mere", "Ana are pere"
#
# rezultat = functia_mea(1,2)
# print(rezultat)

#  Tuplul este o structură de date ordonată și immutable (nu poate fi modificată).
# • Permite elemente duplicat.
# • Este definit folosind parantezele rotunde ( ).

# prima pereche de identificatori de tip este pentru parametrii de intrare, a doua pentru parametrii de iesire

# def suma(a: int, b: int) -> (int, int): #aici, tipul parametrului este o 'sugestie', nu o 'definitie'
#     return a + b, a - b
#
# rezultat_suma, rezultat_dif = suma(1,2)
#
# print(rezultat_suma, rezultat_dif)

# def suma(a: int = 1, b: int = 2) -> (int, float):
#     return a + b, a - b
#
# # rezultat_suma, rezultat_dif = suma(1, 3) #parametrii pozitionali
# rezultat_suma, rezultat_dif = suma(b = 3) #parametrii tip cheie-valoare
# print(rezultat_suma, rezultat_dif)


# def suma(a: int = 1, b: int = 2, c: int = 3, *args) -> (int, float):
#
#     print(type(args))
#     suma = a + b + c
#     for i in args:
#         print(i)
#         suma = suma + i
#     return suma, a - b
#
# rezultat_suma, rezultat_dif = suma(1,2,3, 4, 5, 6, 7, 8, 9, 10) #valorile lui args trebuie sa fie separate prin virgula
# print(rezultat_suma, rezultat_dif)

# def suma(a: int = 1, b: int = 2, c: int = 3, *args) -> (int, float):
#
#     print(type(args))
#     suma = a + b + c
#     for i in args:
#         print(i)
#         suma = suma + i
#     return suma, a - b
#
# rezultat_suma, rezultat_dif = suma(5, 10, 15, 1, 2, 3) #valorile lui args trebuie sa fie separate prin virgula
# print(rezultat_suma, rezultat_dif)

def suma(a: int = 1, b: int = 2, c: int = 3, *args, **kwargs) -> (int, float):

    print(type(kwargs))
    # print(kwargs['d'])

    suma = a + b + c

    for i in args:

        print(i)

        suma = suma + i

    for i in kwargs.values():

        suma = suma + i

    return suma, a - b

rezultat_suma, rezultat_dif = suma(5, 10, 15, 1, 2, 3, d=5, e=6) #cheie valoare pentru kwargs
print(rezultat_suma, rezultat_dif)


