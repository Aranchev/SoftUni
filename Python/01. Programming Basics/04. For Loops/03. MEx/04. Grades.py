a = int(input())  #! бр. студенти
b = 0
c = 0
d = 0
e = 0
B = 0

for i in range(a):
    A = float(input())  #! оценка
    B += A 

    if A >= 2.00 and A <= 2.99:
        b += 1
    if A >= 3.00 and A <= 3.99: 
        c += 1
    if A >= 4.00 and A <= 4.99: 
        d += 1
    if A >= 5.00:
        e += 1

e_p = e / a * 100
d_p = d / a * 100
c_p = c / a * 100
b_p = b / a * 100

print(f"Top students: {e_p:.2f}%")
print(f"Between 4.00 and 4.99: {d_p:.2f}%")
print(f"Between 3.00 and 3.99: {c_p:.2f}%")
print(f"Fail: {b_p:.2f}%")
print(f"Average: {B/a:.2f}")
