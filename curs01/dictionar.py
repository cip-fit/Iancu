# structura de date nordonata, mutabila, indexata.

dic =  {1: "Ana", "2": 'Mere', "3": 'pere', 4: "prune", 1: "Antonia"}
print(dic)
# print(type(dic)) #aici avem chei si valori

#acesta, la printare, v-a prelua valorile intr-o ordine in functie de cheia unica

# print(dic["2"])
# print(dic["22"]) #eroare pentru ca aceasta cheie nu exista

# print(dic.get("22")) #fara eroare, dar o sa afiseze 'None'

# print(dic.get("22", "Nu gaseste nimic"))

# dic["22"] = "valoare noua"
# dic.update({"22": "Val n", "33": 'Alta val'})
# print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())
