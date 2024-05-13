# https://judge.softuni.org/Contests/Practice/Index/1658#5

import math

A = int(input()) * 3.25 # бр. магнолии
B = int(input()) * 4 # бр. зюмбюли
C = int(input()) * 3.50 # бр. рози
d = int(input()) * 8 # бр. кактуси
D = float(input()) # цена на подаръка

e = A + B + C + d - ((A + B + C + d) * 0.05) # данък 

if D < e:
    print(f'She is left with {math.floor(e - D)} leva.')
if D >= e:
    print(f'She will have to borrow {math.ceil(D - e)} leva.')








