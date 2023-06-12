"""
Convertor de timp V2

Scrie un program care preia timpul introdus de utilizator în următorul format:
"11:20 PM" sau "02:00 AM".
Și îl convertește în formatul de 24 de ore.
"23:20" sau "02:00"

Combină soluția cu soluția din lecția live
și permite utilizatorului să decidă ce conversie să facă.
De la 24 de ore la 12 ore, sau invers.
"""

time_str = input("Introduceți timpul în formatul HH:MM AM/PM: ")
conversion_choice = input("Introduceți 1 pentru conversia la formatul de 24 de ore, sau 2 pentru conversia la formatul de 12 ore: ")

if conversion_choice == "1":
    converted_time = convert_time(time_str)
    print("Timpul convertit: {}".format(converted_time))
elif conversion_choice == "2":
    converted_time = convert_time(time_str)
    print("Timpul convertit: {}".format(converted_time + " " + ("AM" if int(converted_time[:2]) < 12 else "PM")))
else:
    print("Opțiunea introdusă nu este validă.")