# https://judge.softuni.org/Contests/Compete/Index/2416#2
a = str(input().lower()) # Вид цветя 
b = int(input())         # Брой цветя 
c = int(input())         # Бюджет 

if a == 'roses':
    d = b * 5
    if b > 80:
        d = d - (d * 0.1)
elif a == 'dahlias':
    d = b * 3.80
    if b > 90:
        d = d - (d * 0.15)
elif a == 'tulips':
    d = b * 2.80
    if b > 80:
        d = d - (d * 0.15)
elif a == 'narcissus':
    d = b * 3
    if b < 120:
        d = d + (d * 0.15)
elif a == 'gladiolus':
    d = b * 2.50
    if b < 80:
        d = d + (d * 0.2)

if c >= d:
    print(f'Hey, you have a great garden with {b} {a.title()} and {c - d:.2f} leva left.')

elif c < d:
    print(f'Not enough money, you need {d - c:.2f} leva more.')
