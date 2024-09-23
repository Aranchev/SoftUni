a = int(input()) # lost fights count
b = float(input()) # helmet price
c = float(input()) # sword price
d = float(input()) # shield price
e = float(input()) # armor price
f = 0 # expenses
g = 0

for i in range(1, a + 1):
    if i % 2 == 0:
        f += b
    if i % 3 == 0:
        f += c
    if i % 2 == 0 and i % 3 == 0:
        f += d
        g += 1
        if g == 2:
            f += e
            g = 0
print(f'Gladiator expenses: {f:.2f} aureus')


