# https://judge.softuni.org/Contests/Compete/Index/2416#1
a = int(input())
b = str(input().lower())

if b == 'morning':
    if 10 <= a <= 18:
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
    elif 18 < a <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif a >= 25:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'

if b == 'afternoon':
    if 10 <= a <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif 18 < a <= 24:   
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    elif a >= 25: 
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'

if b == 'evening':
    if 10 <= a <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif 18 < a <= 24:   
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif a >= 25: 
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

print(f"It's {a} degrees, get your {Outfit} and {Shoes}.")

