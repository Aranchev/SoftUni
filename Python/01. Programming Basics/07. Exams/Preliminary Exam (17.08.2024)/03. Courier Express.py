a = float(input())
b = input()
c = int(input())
d = 0
if b == 'standard':
    if a < 1:
        d += c * 3
    elif a >= 1 and a < 10:
        d += c * 5
    elif a >= 10 and a < 40:
        d += c * 10
    elif a >= 40 and a < 90:
        d += c* 15
    elif a >= 90 and a < 150:
        d += c * 20

elif b == 'express':
    if a < 1:
        d += c * 3
        d += c * (a * (3 * 0.8))
    elif a >= 1 and a < 10:
        d += c * 5
        d += c * (a * (5 * 0.4))
    elif a >= 10 and a < 40:
        d += c * 10
        d += c * (a * (10 * 0.05))
    elif a >= 40 and a < 90:
        d += c * 15
        d += c * (a * (15 * 0.02))
    elif a >= 90 and a < 150:
        d += c * 20
        d += c * (a * (20 * 0.01))

print(f'The delivery of your shipment with weight of {a:.3f} kg. would cost {d/100:.2f} lv.')
