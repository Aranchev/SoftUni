# https://judge.softuni.org/Contests/Practice/Index/1658#4
import math
A = int(input())    # брой дни
B = int(input())    # оставена храна в килограми
C = float(input())  # храна на ден за кучето в килограми
d = float(input())  # храна на ден за котката в килограми
D = float(input()) / 1000  # храна на ден за костенурката в грамове
if B >= (C + d + D) * A:
    print(f'{math.floor(B - ((C + d + D) * A))} kilos of food left.')
else:
    print(f'{math.ceil(((C + d + D) * A) - B)} more kilos of food are needed.')
