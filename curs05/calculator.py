# def parametru(a):
#
#     b = input(f'{a} este: ')
#
#     while b.isdigit() is False:
#         b = input(f'{a} este: ')
#     return int(a)
#
# def validare_operand(plusminus):
#
#     while plusminus not in "+-/*":
#         plusminus = input(f'Operatorul este: ')
#     return plusminus
#
# def suma(c:int,d:int):
#     return c + d
#
# def dif(c:int,d:int):
#     return c - d
#
# def multiply(c:int,d:int):
#     return c * d
#
# def div(c:int,d:int):
#     return c / d
#
# def principal():
#
#     op1 = parametru(1)
#     op2 = parametru(2)
#     operand = input('Operatorul este: ')
#     operator_3 = validare_operand(operand)
#
#     if operator_3 == '+':
#         rez_1 = suma(op1, op2)
#     elif operator_3 == '-':
#         rez_1 = dif(op1, op2)
#     elif operator_3 == '*':
#         rez_1 = multiply(op1, op2)
#     else:
#         rez_1 = div(op1,op2)
#     return rez_1
#
# print(principal())

def parametru(a):
    b = input(f'{a} este: ')
    while not b.isdigit():
        b = input(f'{a} este: ')
    return int(b)  # Return b, not a

def validare_operand(plusminus):
    while plusminus not in "+-/*":
        plusminus = input('Operatorul este: ')
    return plusminus

def suma(c: int, d: int):
    return c + d

def dif(c: int, d: int):
    return c - d

def multiply(c: int, d: int):
    return c * d

def div(c: int, d: int):

    while d == 0:
        d = parametru(2)
    return c / d

def principal():

    op1 = parametru(1)
    op2 = parametru(2)
    operand = input('Operatorul este: ')
    operator_3 = validare_operand(operand)

    if operator_3 == '+':
        rez_1 = suma(op1, op2)
    elif operator_3 == '-':
        rez_1 = dif(op1, op2)
    elif operator_3 == '*':
        rez_1 = multiply(op1, op2)
    elif operator_3 == '/':  # Added division case
        rez_1 = div(op1, op2)
    return rez_1

print(principal())