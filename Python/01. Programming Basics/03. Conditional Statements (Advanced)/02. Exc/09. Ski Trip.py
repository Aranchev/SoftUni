# https://judge.softuni.org/Contests/Compete/Index/2416#8
a = int(input()) # дни за престой
b = str(input().lower()) # вид помещение
c = str(input().lower()) # оценка

d = 18.00 # room for one person
e = 25.00 # apartment
f = 35.00 # president apartment

g = 0

if b == 'room for one person':
    g = (a - 1) * d
elif b == 'apartment':
    if a < 10:
        g = ((a - 1) * e)
        g -= g * 0.3
    elif a >= 10 and a <= 15:
        g = ((a - 1) * e)
        g -= g * 0.35
    elif a > 15:
        g = ((a - 1) * e)
        g -= g * 0.5
elif b == 'president apartment':
    if a < 10:
        g = ((a - 1) * f)
        g -= g * 0.1
    elif a >= 10 and a <= 15:
        g = ((a - 1) * f)
        g -= g * 0.15
    elif a > 15:
        g = ((a - 1) * f)
        g -= g * 0.2

if c == 'positive':
    g += g * 0.25
elif c == 'negative':
    g -= g * 0.1

print(f'{g:.2f}')