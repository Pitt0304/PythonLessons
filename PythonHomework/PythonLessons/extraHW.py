# Exercițiul 1:
# Atribuirea variabilelor
# Scrie un program care atribuie valori celor două variabile,
# a și b, și apoi schimbă valorile lor.
# Afișează valorile lui a și b înainte și după schimbare.

a = 7
b = 8
print(a, b)
tmp1 = b
tmp2 = a
a = tmp1
b = tmp2
print(a, b)
#============================================================================================
# Exercițiul 2: Operații numerice
# Scrie un program care preia două numere ca intrare și efectuează următoarele operații:
#
# Adună cele două numere și afișează rezultatul.
# Scade al doilea număr din primul număr și afișează rezultatul.
# Înmulțește cele două numere și afișează rezultatul.
# Împarte primul număr la al doilea număr și afișează rezultatul.

a = int(input('Introduce un numar: '))
b = int(input('Introducw al doileanumar: '))

print(a + b)
print(a - b)
print(a * b)
print(a / b)