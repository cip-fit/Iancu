a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Rezultat [1,2,3,5,8,13]

c=set()

for i in b:
    if i in a:
        c.add(i)
c=list(c)
print(c)