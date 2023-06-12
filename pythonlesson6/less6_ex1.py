"""
Calculator BMI
Scrie un program care primește greutatea unei persoane (în kilograme) și înălțimea (în metri) ca intrare și calculează Indicele de Masă Corporală (BMI). Apoi clasifică BMI-ul în următoarele categorii:

Subponderal (BMI < 18,5)
Greutate normală (BMI între 18,5 și 24,9)
Supraponderal (BMI între 25 și 29,9)
Obezitate (BMI 30 sau mai mare)

Pentru a calcula Indicele de Masă Corporală (BMI), urmează pașii de mai jos:

1. Ia greutatea persoanei în kilograme și înălțimea în metri.
2. Calculează pătratul înălțimii (înmulțește înălțimea cu ea însăși).
3. Calculează BMI-ul utilizând formula: BMI = greutate / înălțime^2, unde greutatea este în kilograme și înălțimea este în metri.
4. Rezultatul obținut va fi indicele de masă corporală al persoanei.

"""
weight = int(input("Introduceti greutatea in kilograme: "))
height = float(input("Introduceti inaltimea in metri: "))
patratul = float(height ** 2)
patratul_round = round(patratul, 1)
print(patratul)
bmi = float(weight / patratul)
bmi_round = round(bmi, 1)

print("indicele de masă corporală al persoanei este: ", {bmi_round})

if bmi_round < 18.5:
    print("Subponderal")
elif bmi_round >=18.5 and bmi_round <= 24.9:
    print("Greutate normală")
elif bmi_round >=25 and bmi_round <= 29.9:
    print("Supraponderal")
else:
    print("Obezitate")

