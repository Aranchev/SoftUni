# https://judge.softuni.org/Contests/Compete/Index/2416#4
a = float(input()) # бюджет
b = str(input().lower()) # сезон

if a <= 100:
    c = 'Bulgaria'
    if b == 'summer':
        d = 'Camp'
        f = a * 0.3
    elif b == 'winter':
        d = 'Hotel'
        f = a * 0.7
elif a <= 1000:
    c = 'Balkans'
    if b == 'summer':
        d = 'Camp'
        f = a * 0.4
    if b == 'winter':
        d = 'Hotel'
        f = a * 0.8
elif a > 1000:
    c = 'Europe'
    d = 'Hotel'
    f = a * 0.9

print(f'Somewhere in {c}\n{d} - {f:.2f}')