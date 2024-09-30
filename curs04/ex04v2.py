"""
Sa da de la tastatura un string. Sa se elimine caracterele din string pornind de la 0 pana la n,
unde n e dat si el de la tastatura
"""

s = input('sir: ')
n = input('n: ')

if n.isdigit():
    n = int(n)

    if n <= len(s):
        s = s[n:]
        print(s)