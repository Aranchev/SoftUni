# https://judge.softuni.org/Contests/Practice/Index/1663#4
# Вход --------------------------------------------------------------
a = float(input())              # Бюджет – реално число в интервала
b = str(input().lower())        # Сезон – текст "Summer" или "Winter"
# -------------------------------------------------------------------
if a <= 1000:
    c = 'Camp'
    if b == 'summer':
        d = 'Alaska'
        e = a * 0.65
    elif b == 'winter':
        d = 'Morocco'
        e = a * 0.45
elif a >= 1000 and a <= 3000:
    c = 'Hut'
    if b == 'summer':
        d = 'Alaska'
        e = a * 0.8
    elif b == 'winter':
        d = 'Morocco'
        e = a * 0.6
elif a > 3000:
    c = 'Hotel'
    if b == 'summer':
        d = 'Alaska'
        e = a * 0.9
    elif b == 'winter':
        d = 'Morocco'
        e = a * 0.9
# Изход -------------------------------------------------------------
print(f'{d} - {c} - {e:.2f}')

