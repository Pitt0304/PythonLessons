"""
Scrieţi un program care citeşte de la tastatură numele unei persoane.
Dacă numele nu începe cu literă mare, atunci programul transformă valoarea citită în numele persoanei scris cu literă mare.
După aceasta, afişează la ecran `"Salut, <numele citit de la tastatura care începe cu litera mare>!"`.
"""

nume = input("Introduceți numele unei persoane: ")

if not nume[0].isupper():
    nume = nume.capitalize()

print("Salut,", nume + "!")

#nu meam dat seama cum si lam facut cu ChatGPT