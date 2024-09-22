# Avand doua liste, afisati o lista a elementelor comune ambelor liste

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Rezultat [1,2,3,5,8,13]

c={}

for i in a:
    if i in b:
        a1=set(a)
        b1=set(b)
        c = a1.intersection(b)
        c = list(c)
print(c)









