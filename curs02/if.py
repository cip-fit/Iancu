
in if se pot folosi mai multe if-uri

nr1 = 4 #nr1: 4

total, salariu = None, "Salariu mic"
print(salariu)

if nr1 <= 4 and (salariu := "Salariu mare"): #variabila salariu poate fi folosita numai in acest bloc
    total = nr1 + 1
    salariu = "Salariu"
elif nr1 < 2:
    total = nr1 + 2

print(total)
print(salariu)
