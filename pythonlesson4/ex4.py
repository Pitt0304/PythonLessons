"""
Scrieţi un program care verifică dacă litera "a" se află pe a 2-a poziţie într-un String citit de la tastatură.
"""

string = input("Introduceți un sir de caractere: ")

if len(string) >= 2 and string[1] == "a":
    print("Litera 'a' se afla pe a doua poziție în șirul introdus.")
else:
    print("Litera 'a' nu se afla pe a doua poziție în șirul introdus.")


string2 = input("Introduceți un sir de caractere: ")

if string2[1] == "a":
    print("Litera 'a' se afla pe a doua poziție în șirul introdus.")
else:
    print("Litera 'a' nu se afla pe a doua poziție în șirul introdus.")