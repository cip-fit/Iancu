a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
b = ['banana', 'kiwi', 'apple', 'apple', 'grape']

# Step 1: Count occurences in list a
c = {}
for i in a:
    c[i] = c.get(i, 0) + 1 # Count each item

# Step 2: Create a set for unique intersection items
d = set()
for i in b:
    if i in c:
        d.add(i)

d = list(d)
print(d)


