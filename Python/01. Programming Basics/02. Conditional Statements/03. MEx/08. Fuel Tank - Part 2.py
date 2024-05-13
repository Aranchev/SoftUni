# https://judge.softuni.org/Contests/Practice/Index/1658#7

A = 2.22 # лева за литър бензин
a = 0.18 # отстъпка за литър 

B = 2.33 # лева за литър дизел
b = 0.12 # отстъпка за литър 

C = 0.93 # лева за литър газ
c = 0.08  # отстъпка за литър

D = str(input().lower()) # Типа на горивото - "Gas", "Gasoline" или "Diesel"
d = int(input())         # Количество гориво
E = str(input().lower()) # Притежание на клубна карта – текст с възможности: "Yes" или "No"


if D == 'gasoline':
    f = d * A
    if E == 'yes':
        f -= d * a

elif D == 'diesel':
    f = d * B
    if E == 'yes':
        f -= d * b

elif D == 'gas':
    f = d * C
    if E == 'yes':
        f -= d * c

if d >= 20 and d <= 25:
    f -=  f * 0.08
elif d > 25:
    f -= f * 0.1

    

print(f"{f:.2f} lv.")





