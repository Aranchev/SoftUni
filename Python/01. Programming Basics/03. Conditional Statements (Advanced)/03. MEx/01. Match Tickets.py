# https://judge.softuni.org/Contests/Practice/Index/1663#0
#ВХОД: - 3 реда --------------------------------------------
a = float(input())              # бюджетът
b = str(input().lower())        # категорията - "VIP" или "Normal"
c = int(input())                # броят на хората в групата
# -----------------------------------------------------------
A = 499.99                      # VIP 
B = 249.99                      # Normal 
#------------------------------------------------------------
C = 0                           # транспорт
#------------------------------------------------------------
if b == 'vip':
    if c >= 1 and c <= 4:       # транспорт
        C += a * 0.75
    elif c >= 5 and c <= 9:
        C += a * 0.6
    elif c >= 10 and c <= 24:
        C += a * 0.5
    elif c >= 25 and c <= 49:
        C += a * 0.4
    elif c >= 50:
        C += a * 0.25
    d = a - C
    D = d - (c * A) 
    if D >= 0:
        print(f'Yes! You have {D:.2f} leva left.')
    elif D < 0:
        print(f'Not enough money! You need {abs(D):.2f} leva.')
elif b == 'normal':
    if c >= 1 and c <= 4:       # транспорт
        C += a * 0.75
    elif c >= 5 and c <= 9:
        C += a * 0.6
    elif c >= 10 and c <= 24:
        C += a * 0.5
    elif c >= 25 and c <= 49:
        C += a * 0.4
    elif c >= 50:
        C += a * 0.25
    d = a - C
    D = d - (c * B) 
    if D >= 0:
        print(f'Yes! You have {D:.2f} leva left.')
    elif D < 0:
        print(f'Not enough money! You need {abs(D):.2f} leva.')
