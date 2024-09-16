# print("Hello, World!")

# print(3, type(3))
# print(3.14, type(3.14))
# print(3+1j, type(3+1j))

# print(float(4))
# print(int(3.5))

# print(3*5.4)
# print(5/2)
# print(5//2)
# print(5%2)
# print(5**2)

# Boolean = { 0 = False; 1 = True }

# print(5**2)
# print(5==2)
# print(5==5)
# print(5!=5)
# print(5>5)
# print(5>=5)
# print(5<=5)
# print(5<5)

# print(4<5 and 3>2)

"""
    operatorul AND
    True and True => True
    True and False => False
    False and True => False
    False and False => False
"""
# print(4<5 or 3<4)
"""
    operatorul OR
    True or True => True
    True or False => True
    False or True => True
    False or False => False
"""
# print(not(4<5))
"""
    operatorul NOT
    not(True) => False
    not(False) => True
"""
# print("a" in "python")
"""
    operatorul in = apartenenta
    evalueaza True sau False
"""
# a = 1 # definim variabila simplu
"""
    snake_case inseamna ca folosim underscore cand definim o variabila, adica variabila_1 = 1
    denumirile cu litera mare sunt pentru denumiri de clase
    nu incepem declararea unei variabile cu un numar
"""
variabila_1 = None
print(type(variabila_1))

variabila = "Ana are mere"
print(type(variabila))

numar_mere=2
variabila1 = 'V1 Ana are ' + str(numar_mere) + ' mere'

numar_pere=3
variabila2 = f"V2 Ana are {numar_mere} mere si {numar_pere} pere"
print(variabila1)
print(variabila2)

variabila3 = "V3 Ana are {0} mere si {1} pere".format(numar_mere, numar_pere)
print(variabila3)

variabila4 = "V4 Ana are \"{}\" mere si \"{}\" pere".format(numar_mere, numar_pere)
print(variabila4)

variabila5 = "V5 Ana are '{}' mere si \t'{}' pere".format(numar_mere, numar_pere)
print(variabila5)



