date_personale = list()
info_date = ["nume", "prenume", "age", "ocupatie"]
for el in info_date:
    info = input(f"intoduceti {el}: ")
    date_personale.append(info)

print(f"lista cu datele personale: {date_personale}")

#am incercat singur sa fac
telefoane = list()
info_telefoane = ['marka', 'culoarea', 'pretul', 'magazin']

for el in info_telefoane:
    info = input(f" Introduceti datele {el}: ")
    telefoane.append(info)

print(f" Lista datelor de telefoane: {telefoane}")

#am copiat, nu inteleg de loc ciclul for