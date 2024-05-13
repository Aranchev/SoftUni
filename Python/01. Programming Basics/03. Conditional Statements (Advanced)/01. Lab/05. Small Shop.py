# https://judge.softuni.org/Contests/Compete/Index/2415#4
a = str(input().lower())
b = str(input().lower())
c = float(input())

if b == 'sofia':
    if a == 'coffee':
        f = c * 0.50
    elif a == 'water':
        f = c * 0.80
    elif a == 'beer':
        f = c * 1.20
    elif a == 'sweets':
        f = c * 1.45
    elif a == 'peanuts':
        f = c * 1.60
    
elif b == 'plovdiv':
    if a == 'coffee':
        f = c * 0.40
    elif a == 'water':
        f = c * 0.70
    elif a == 'beer':
        f = c * 1.15
    elif a == 'sweets':
        f = c * 1.30
    elif a == 'peanuts':
        f = c * 1.50
elif b == 'varna':
    if a == 'coffee':
        f = c * 0.45
    elif a == 'water':
        f = c * 0.70
    elif a == 'beer':
        f = c * 1.10
    elif a == 'sweets':
        f = c * 1.35
    elif a == 'peanuts':
        f = c * 1.55

print(f)