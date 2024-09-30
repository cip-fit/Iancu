"""
Sa da de la tastatura un string. Sa se elimine caracterele din string pornind de la 0 pana la n,
unde n e dat si el de la tastatura
"""

sir = input('sir: ')
n = int(input('n: '))
a = len(sir)
sir_n = ''

for i in range(a):

    if i > int(n-1):

        sir_n += sir[i]

print(sir_n)