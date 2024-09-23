a = int(input())

b = []

c = []

for i in range(a):
    d = int(input())
    b.append(d)

e = input()

if e == 'even':
    for i in b:
        if i % 2 == 0:
            c.append(i)
elif e == 'odd':
    for i in b:
        if i % 2 != 0:
            c.append(i)
elif e == 'negative':
    for i in b:
        if i < 0:
            c.append(i)
elif e == 'positive':
    for i in b:
        if i >= 0:
            c.append(i)
print(c)
