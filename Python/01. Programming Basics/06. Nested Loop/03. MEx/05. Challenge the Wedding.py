a = int(input())
b = int(input())
c = int(input())
d = 0
f = a * b

for A in range(1, a + 1):
    for B in range(1, b + 1):
        if d == c or d == f:
            break
        d += 1
        print(f'({A} <-> {B})', end=' ')

