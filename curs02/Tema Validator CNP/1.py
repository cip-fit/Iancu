"""
Se doreste realizarea unui validator de CNP.

✅ CNP must be 13 digits long.
✅ Sex and Century (S)

✅1/2: 1900-1999
✅3/4: 1800-1899
✅5/6: 2000-2099
✅7/8: Foreign residents (20th century)
✅9: Foreigners

✅Last 2 digits of birth year.
✅Valid month (01-12).
✅Valid day (01-31, with leading zero).
✅Valid code for county or Bucharest (41-46).

✅Control Digit (C)
✅Calculate based on first 12 digits.
✅Compare with 13th digit.
✅Final Check

✅All checks must pass for valid CNP.
"""
judete = {
    '01': 'Alba',
    '02': 'Arad',
    '03': 'Argeș',
    '04': 'Bacău',
    '05': 'Bihor',
    '06': 'Bistrița-Năsăud',
    '07': 'Botoșani',
    '08': 'Brașov',
    '09': 'Brăila',
    '10': 'Buzău',
    '11': 'Caraș-Severin',
    '12': 'Cluj',
    '13': 'Constanța',
    '14': 'Covasna',
    '15': 'Dâmbovița',
    '16': 'Dolj',
    '17': 'Galați',
    '18': 'Gorj',
    '19': 'Harghita',
    '20': 'Hunedoara',
    '21': 'Ialomița',
    '22': 'Iași',
    '23': 'Ilfov',
    '24': 'Maramureș',
    '25': 'Mehedinți',
    '26': 'Mureș',
    '27': 'Neamț',
    '28': 'Olt',
    '29': 'Prahova',
    '30': 'Satu Mare',
    '31': 'Sălaj',
    '32': 'Sibiu',
    '33': 'Suceava',
    '34': 'Teleorman',
    '35': 'Timiș',
    '36': 'Tulcea',
    '37': 'Vaslui',
    '38': 'Vâlcea',
    '39': 'Vrancea',
    '40': 'București',
    '41': 'București S.1',
    '42': 'București S.2',
    '43': 'București S.3',
    '44': 'București S.4',
    '45': 'București S.5',
    '46': 'București S.6',
    '51': 'Călărași',
    '52': 'Giurgiu'
}

lunile_anului = {
    "01": "Ianuarie",
    "02": "Februarie",
    "03": "Martie",
    "04": "Aprilie",
    "05": "Mai",
    "06": "Iunie",
    "07": "Iulie",
    "08": "August",
    "09": "Septembrie",
    "10": "Octombrie",
    "11": "Noiembrie",
    "12": "Decembrie"
}

CNP = input('Introduceti CNP: ')

# Verificarea daca CNP-ul contine 13 caractere -- atentie: nu se verifica daca sunt 13 numere, ci doar 13 caractere
if len(CNP) != 13:
    print(f'Codul CNP introdus este invalid.')

else:

    cifra_control = "279146358279"
    suma = 0

    # Contorizam un i de 12 ori pentru a inmulti cele 2 numere: cand i = 0, se va inmulti primul caracter al CNP cu primul caracter al cifra_control
    for i in range(12):

        # Am impus ca itemii de inmultit sa fie numere intregi pentru ca altfel nu functioneaza (se inmulteau string-urile)
        produs = int(CNP[i]) * int(cifra_control[i])

        # Aici adunam produsul celor doi itemi de inmultit: adica pentru i = 0, se aduna CNP[0] * cifra_control[0] la suma
        suma += produs

    # Atribuim un rest
    rest = suma % 11

    # Atribuim cifrei de calculat 1 sau restul
    if rest == 10:
        cifra_c_calc = 1
    else:
        cifra_c_calc = rest

    # Extragem cifra de verificare
    cifra_de_verificat = CNP[-1]

    # Se verifica daca CNP-ul este real validand ultima cifra a acestuia
    # Programul nu mergea daca nu le facem numere intregi
    if int(cifra_de_verificat) == int(cifra_c_calc):
        print(f'Codul {CNP} este un cod CNP valid.')
    else:
        print(f'Codul {CNP} este un cod CNP invalid.')

    judet_cheie = CNP[7:9]
    judet_val = judete.get(judet_cheie, 'Necunoscut')

    luna_cheie = CNP[3:5]
    luna_val = lunile_anului.get(luna_cheie, 'Necunoscuta')

    if CNP[0] == '1':
        print(
            f'CNP-ul corespunde unui barbat nascut in anul 19{CNP[1:3]}, luna {luna_val}, ziua {CNP[5:7]} si judetul {judet_val}.')
    elif CNP[0] == '2':
        print(
            f'CNP-ul corespunde unei femei nascute in anul 19{CNP[1:3]}, luna {luna_val}, ziua {CNP[5:7]} si judetul {judet_val}.')
    elif CNP[0] == '3':
        print(
            f'CNP-ul corespunde unui barbat nascut in anul 18{CNP[1:3]}, luna {luna_val}, ziua {CNP[5:7]} si judetul {judet_val}. 💀')
    elif CNP[0] == '4':
        print(
            f'CNP-ul corespunde unei femei nascute in anul 18{CNP[1:3]}, luna {luna_val}, ziua {CNP[5:7]} si judetul {judet_val}. 💀')
    elif CNP[0] == '5':
        print(
            f'CNP-ul corespunde unui barbat nascut in anul 20{CNP[1:3]}, luna {luna_val}, ziua {CNP[5:7]} si judetul {judet_val}.')
    elif CNP[0] == '6':
        print(
            f'CNP-ul corespunde unei femei nascute in anul 20{CNP[1:3]}, luna {luna_val}, ziua {CNP[5:7]} si judetul {judet_val}.')
    elif CNP[0] == '7':
        print(
            f'CNP-ul corespunde unui barbat strain rezident in Romania nascut in anul --{CNP[1:3]}, luna {luna_val}, ziua {CNP[5:7]} si judetul {judet_val}.')
    elif CNP[0] == '8':
        print(
            f'CNP-ul corespunde unei femei straine rezidente in Romania nascute in anul --{CNP[1:3]}, luna {luna_val}, ziua {CNP[5:7]} si judetul {judet_val}.')
    elif CNP[0] == '9':
        print(
            f'CNP-ul corespunde unei persoane straine nascute in anul --{CNP[1:3]}, luna {luna_val}, ziua {CNP[5:7]} si judetul {judet_val}.')
