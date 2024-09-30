"""
Create a Python script that fulfills the following functions:

✅ Declare a list that contains the elements 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (in this order).
✅ Display the initial list sorted in ascending order (the initial list must remain unchanged).
✅ Display the initial list sorted in descending order (the initial list must remain unchanged).
✅ Display a list containing the even numbers from the sorted list (using slicing).
✅ Display a list containing the odd numbers from the sorted list (using slicing).
✅ Display a list containing the numbers that are multiples of 3 (using slicing).

"""



lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

a = sorted(lista)
print(a)

# Length of the list to determine how many times to loop
a = len(lista)
b=lista

# OL: Allows us to access 0 to n-1 / i becomes 0, 1, 2, 3
for i in range(a):

    # IL: Starts from i+1 up to end of the list
    for j in range(i + 1, a):

        # Compare first element with the second
        if b[i] < b[j]:

            # For i=0, j=1: list[i] = 7, list[j] = 8
            b[i], b[j] = b[j], b[i]


# Print list in a descending order
print(b)

b = len(lista)

c=[]
d=[]

for i in range(b):
    if lista[i] % 2 == 0:
        c.append(lista[i])
    else:
        d.append(lista[i])
# c.sort()
# print(c)
print(sorted(c))
print(sorted(d))

e=[]

for i in range(b):
    if lista[i] % 3 == 0:
        e.append(lista[i])
    else:
        pass

print(sorted(e))