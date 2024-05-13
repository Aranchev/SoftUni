# https://judge.softuni.org/Contests/Practice/Index/1663#6
a = str(input().lower()) # Сезонът –“Winter”, “Spring” или “Summer”
b = str(input().lower()) # Видът на групата – “boys”, “girls” или “mixed”;
c = int(input()) # Брой на учениците 
d = int(input()) # Брой на нощувките 

if a == 'winter':
    if b == 'boys' or 'girls':
        A = 9.60    # цена на нощувка
        if b == 'girls':
            C = 'Gymnastics' # спорт
        elif b == 'boys':
            C = 'Judo'
        elif b == 'mixed':
            A = 10
            C = 'Ski'
    B = c * d * A   # цена изобщо
    if c >= 50:
        B -= B * 0.5
    elif c >= 20 and c < 50:
        B -= B * 0.15
    elif c >= 10 and c < 20:
        B -= B * 0.05
        
elif a == 'spring':
    if b == 'boys' or 'girls':
        A = 7.20    # цена на нощувка
        if b == 'girls':
            C = 'Athletics' # спорт
        elif b == 'boys':
            C = 'Tennis'
        elif b == 'mixed':
            A = 9.50
            C = 'Cycling'
    B = c * d * A   # цена изобщо
    if c >= 50:
        B -= B * 0.5
    elif c >= 20 and c < 50:
        B -= B * 0.15
    elif c >= 10 and c < 20:
        B -= B * 0.05
        
elif a == 'summer':
    if b == 'boys' or 'girls':
        A = 15    # цена на нощувка
        if b == 'girls':
            C = 'Volleyball' # спорт
        elif b == 'boys':
            C = 'Football'
        elif b == 'mixed':
            A = 20
            C = 'Swimming'
    B = c * d * A   # цена изобщо
    if c >= 50:
        B -= B * 0.5
    elif c >= 20 and c < 50:
        B -= B * 0.15
    elif c >= 10 and c < 20:
        B -= B * 0.05

print(f'{C} {B:.2f} lv.')