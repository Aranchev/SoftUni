a = int(input()) 
b = int(input())
c = int(input())

z, x, y = 0, 1, 1

A = 35
B = 64

while True:
    print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end='|')
    A += 1
    B += 1
    y += 1
    z += 1

    if y == b + 1: 
        x += 1
        y = 1
    if x == a + 1:
        break
    if y == b + 1:
        break
    if z == c:
        break
    if A == 55 + 1:
        A = 35
    if B == 96 + 1:
        B = 64
