cuvant = 'onomatopee'
cuvant_2 = ''
nr_vieti = 7

for i in cuvant:

    if i != cuvant[0] and i != cuvant [-1]:
        cuvant_2 = cuvant_2 + '_'
    else:
        cuvant_2 = cuvant_2 + i

print(cuvant_2)

while cuvant_2 != cuvant and nr_vieti > 0:

    litera_c = input("Alege o litera: ")

    if litera_c in cuvant:
        lista_cuvant_2 = list(cuvant_2)

        for i, v in enumerate(cuvant):

            if v == litera_c:
                lista_cuvant_2[i] = v
        cuvant_2 = "".join(lista_cuvant_2)

    else:
        nr_vieti -=1

        if nr_vieti != 0:
            print(f"Mai ai {nr_vieti} vieti")
    print(cuvant_2)

if nr_vieti == 0:
    print(f"Ai pierdut! Cuvantul era: {cuvant}")