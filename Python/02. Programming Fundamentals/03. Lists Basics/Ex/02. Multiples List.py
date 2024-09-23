a = int(input())
b = int(input())
d = []

for i in range(0, a * b + 1, a):
    if i > 0:
        d += [i]
print(d)
