# https://judge.softuni.org/Contests/Compete/Index/2416#3
a = int(input()) # Бюджет на групата 
b = str(input().lower()) # Сезон 
c = int(input()) # Брой рибари

if b == 'spring':
    if c <= 6:
        d = 3000 - (3000 * 0.1)
    if c >= 7 and c <= 11:
        d = 3000 - (3000 * 0.15)
    if c > 12:
        d = 3000 - (3000 * 0.25)

elif b == 'summer':
    if c <= 6:
        d = 4200 - (4200 * 0.1)
    if c >= 7 and c <= 11:
        d = 4200 - (4200 * 0.15)
    if c > 12:
        d = 4200 - (4200 * 0.25)
    
elif b == 'autumn':
    if c <= 6:
        d = 4200 - (4200 * 0.1)
    if c >= 7 and c <= 11:
        d = 4200 - (4200 * 0.15)
    if c > 12:
        d = 4200 - (4200 * 0.25)
elif b == 'winter':
    if c <= 6:
        d = 2600 - (2600 * 0.1)
    if c >= 7 and c <= 11:
        d = 2600 - (2600 * 0.15)
    if c > 12:
        d = 2600 - (2600 * 0.25)
    

if b != 'autumn' and c % 2 == 0:   
    d -= d * 0.05

if d <= a:
    print(f'Yes! You have {a - d:.2f} leva left.')
elif d > a:
    print(f'Not enough money! You need {d - a:.2f} leva.')
