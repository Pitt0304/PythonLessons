"""
Scrieți un program care cere utilizatorului să introducă o propoziție.
Dacă propoziția se încheie cu un semn de întrebare ("?"),
afișați mesajul „Aceasta este o întrebare”.
În caz contrar, afișați mesajul „Aceasta nu este o întrebare”
"""

text = input('introduce propozitia: ')

if text.endswith("?"):
    print("Aceasta este o întrebare")
else:
    print("Aceasta nu este o intrebare.")

# propozitie = input("Introduceți o propoziție: ")
#
# if propozitie.endswith("?"):
#     print("Aceasta este o întrebare.")
# else:
#     print("Aceasta nu este o întrebare.")