import math
a = int(input())
b = int(input())
c = float(input())
d = float(input())
e = float(input())

f = a * (c+d+e)

if f < b:
    print(f'{math.floor(b-f)} kilos of food left.')
else:
    print(f'{math.ceil(f - b)} more kilos of food are needed.')
