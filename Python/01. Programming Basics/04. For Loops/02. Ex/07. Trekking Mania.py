a = int(input())  #! брой на групите
b = 0  #! Мусала
c = 0  #! Монблан
d = 0  #! Килиманджаро
e = 0  #! К2
f = 0  #! Еверест

for i in range(a):
    g = int(input())
    if g <= 5:  #! Мусала
        b += g
    elif g >= 6 and g <= 12:  #! Монблан
        c += g
    elif g >= 13 and g <= 25:  #! Килиманджаро
        d += g
    elif g >= 26 and g <= 40:  #! К2
        e += g
    elif g >= 41:  #! Еверест
        f += g
        
h = b + c + d + e + f  #! всички хора
b_p = b / h * 100
c_p = c / h * 100
d_p = d / h * 100
e_p = e / h * 100
f_p = f / h * 100

print(f"{b_p:.2f}%")
print(f"{c_p:.2f}%")
print(f"{d_p:.2f}%")
print(f"{e_p:.2f}%")
print(f"{f_p:.2f}%")
