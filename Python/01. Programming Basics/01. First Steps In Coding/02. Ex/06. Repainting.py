# https://judge.softuni.org/Contests/Compete/Index/2424#5
Nailon = (float(input()) + 2) * 1.50

input_za_boq = float(input()) * 14.50
proc_za_boq = input_za_boq * 0.1
Boq = input_za_boq + proc_za_boq

Razreditel = float(input()) * 5.00

Torbichki = 0.40

Zaplata_za_chas_na_maistorite = (Nailon + Boq + Razreditel + Torbichki) * 0.3

chasove_na_rabota = float(input()) * Zaplata_za_chas_na_maistorite

suma = Nailon + Boq + Razreditel + Torbichki + chasove_na_rabota

print(suma)