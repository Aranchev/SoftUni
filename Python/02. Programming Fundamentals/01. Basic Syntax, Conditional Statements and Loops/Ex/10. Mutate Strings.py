a = input()
b = input()
c = a
for e in range(len(a)):
    f = b[:e + 1]
    g = a[e + 1:]
    h = f + g
    if h != c:
        print(h)
        c = h
