a = int(input())
b = int(input())
c = 0
d = 0
for i in range(a, b+1):
    c = 0
    d = 0
    for idx, x in enumerate(str(i), start=1):
        if idx % 2 != 0:
            c += int(x)
        if idx % 2 == 0:
            d += int(x)
    if c - d == 0:
        print(i, end = ' ')
