# https://judge.softuni.org/Contests/Practice/Index/1663#3
# Вход ----------------------------------------------------
a = float(input())              # Бюджет – реално число в интервала 
b = str(input().lower())        # текст "Summer" или "Winter"
#----------------------------------------------------------
if a <= 100:
    c = 'Economy class'         # Class
    if b == 'summer':
        e = 'Cabrio'                # Тип
        E = a * 0.35                # Цена на типът
    elif b == 'winter':
        e = 'Jeep'
        E = a * 0.65
elif a > 100 and a <= 500:
    c = 'Compact class'
    if b == 'summer':
        e = 'Cabrio'                # Тип
        E = a * 0.45                # Цена на типът
    elif b == 'winter':
        e = 'Jeep'
        E = a * 0.8
elif a > 500:
    c = 'Luxury class'
    if b == 'summer':
        e = 'Jeep'
        E = a * 0.9
    elif b == 'winter':
        e = 'Jeep'
        E = a * 0.9
# Изход ---------------------------------------------------
print(f'{c}\n{e} - {E:.2f}')

