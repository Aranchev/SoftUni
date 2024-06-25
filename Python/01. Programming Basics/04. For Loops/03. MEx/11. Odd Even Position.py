import sys

a = int(input())
b = sys.maxsize
c = -sys.maxsize
e = b
f = c
A = 0
B = 0

for i in range(1, a + 1):
    d = float(input())
    if i % 2 != 0:
        A += d
        if d > c:
            c = d
        if d < b:
            b = d
    if i % 2 == 0:
        B += d
        if d > f:
            f = d
        if d < e:
            e = d

print(f'OddSum={A:.2f},')
if b == sys.maxsize and c == -sys.maxsize:
    print('OddMin=No,')
    print('OddMax=No,')
else:
    print(f'OddMin={b:.2f},')
    print(f'OddMax={c:.2f},')

print(f'EvenSum={B:.2f},')
if e == sys.maxsize and f == -sys.maxsize:
    print('EvenMin=No,')
    print('EvenMax=No')
else:
    print(f'EvenMin={e:.2f},')
    print(f'EvenMax={f:.2f}')
