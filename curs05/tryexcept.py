# Try-except reprezinta un bloc de cod care ne ajuta sa evitam anumite situatii


text = input("Adauga un nr: ")

try:

    #aici trecem codul care credem noi ca o sa aiba eroare
    conversie = int(text)
    # daca blocul de executie are o eroare, atunci va executa blocul din except


    #Exception este clasa mare care contine cele mai multe exceptii in python
        #in acest caz, exceptia pe care o inlocuieste este un 'ValueError: '

except ValueError:
    print("Avem o exceptie")

except Exception:
    print("Exceptie generala")

else:
    print(conversie)

finally:
    print('Se executa oricand')

print(text)

#cand folosim try-except: daca data care este introdusa nu exista, atunci cream o data default