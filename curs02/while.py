#structuri repetitive = while, for
"""
while conditie
    bloc de instructiuni
    break = sintaxa care ne scoate automat din for
"""

a = 10
while 1 < a <= 10:
    print(f'Ana are {a} mere')
    if a % 2 == 8:
        continue
    a = a - 1 # sau a -= 1

    # break