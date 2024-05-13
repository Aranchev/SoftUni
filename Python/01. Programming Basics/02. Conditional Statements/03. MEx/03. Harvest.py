# https://judge.softuni.org/Contests/Practice/Index/1658#2

import math
# Вход:
X = int(input())    # X кв.м е лозето 
Y = float(input())  # Y грозде за един кв.м
Z = int(input())    # Z нужни литри вино
W = int(input())    # брой работници

m = X * 0.4
l_of_wine = m * Y / 2.5

if l_of_wine < Z:
    print(f"It will be a tough winter! More {math.floor(Z - l_of_wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.ceil(l_of_wine)} liters.")
    print(f"{math.floor(l_of_wine - Z)} liters left -> {math.ceil((l_of_wine - Z) / W)} liters per person.")