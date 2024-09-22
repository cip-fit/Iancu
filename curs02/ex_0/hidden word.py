
c1=input('Cuvantul de ghicit este: ') # Cuvantul de ghicit
h_c1 = c1[0] + '_' * (len(c1) - 2) + c1[-1]

"""
Cuvantul ascuns este prima si ultima litera
+ underscore de la a doua litera pana la penultima
"""

print('\n' * 20, h_c1) # Printam 20 randuri goale
lives = 7

while c1 != h_c1 and lives > 0: # Cat timp true = (cuv de ghici diferit de cuv ascuns si vieti > 0):

    litera = input('Alege o litera: ')
    lista_h_c1 = list(h_c1) # Transformam lista de ghici in lista

    if litera in c1: # Daca litera este in cuvantul de ghicit:

        for i in range(1, len(c1) - 1): # Pentru fiecare i in numarul de litere al cuvantul de ghicit

            if litera == c1[i]: # Daca contorul potrivit cuvantului este egala cu 'litera''
                lista_h_c1[i] = litera # Atunci adugam listei cuvantului ascuns 'litera'


        h_c1 = ''.join(lista_h_c1) # Adaugam tot continutul ('') cuvantului ascuns litera descoperita anterior

        print(h_c1) # Printam cuvantul ascuns

    else:
        lives -=1
        if lives != 0:
            print(f'Mai ai {lives} vieti')

if h_c1 == c1:
    print(f'Felicitari! Cuvantul este: {h_c1}')
else:
    print(f'Ai pierdut! Cuvantul era: {c1}')





