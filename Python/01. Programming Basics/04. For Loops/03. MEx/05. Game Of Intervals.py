a = int(input())  #! колко хода ще има по време на играт
c = 0
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0

for i in range(a):
    b = int(input())  #! числата, които се проверяват в кой интервал са

    if b >= 0 and b <= 9:
        c += 0.2 * b
        A += 1
    if b >= 10 and b <= 19:
        c += 0.3 * b
        B += 1
    if b >= 20 and b <= 29:
        c += 0.4 * b
        C += 1
    if b >= 30 and b <= 39:
        c += 50
        D += 1
    if b >= 40 and b <= 50:
        c += 100
        E += 1
    if b < 0 or b > 50:
        c /= 2
        F += 1

A_p = A / a * 100
B_p = B / a * 100
C_p = C / a * 100
D_p = D / a * 100
E_p = E / a * 100
F_p = F / a * 100

print(f"{c:.2f}")
print(f"From 0 to 9: {A_p:.2f}%")
print(f"From 10 to 19: {B_p:.2f}%")
print(f"From 20 to 29: {C_p:.2f}%")
print(f"From 30 to 39: {D_p:.2f}%")
print(f"From 40 to 50: {E_p:.2f}%")
print(f"Invalid numbers: {F_p:.2f}%")
