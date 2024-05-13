# https://judge.softuni.org/Contests/Practice/Index/1663#5
a = str(input().lower())
b = float(input())

if b <= 5000:
    if a == 'spring' or a =='autumn':
        c = b * 0.75
    elif a == 'summer':
        c = b * 0.90
    elif a == 'winter':
        c = b * 1.05
    c *= 4
elif b > 5000 and b <= 10000:
    if a == 'spring' or a == 'autumn':
        c = b * 0.95
    elif a == 'summer':
        c = b * 1.10
    elif a == 'winter':
        c = b * 1.25
    c *= 4
elif b > 10000 and b <= 20000:
    c = b * 1.45
    c *= 4

c -= (c * 0.1)

print(f'{c:.2f}')