a = input()
b = []

for i, x in enumerate(a):
    if x.isupper():
        b += [i]
print(b)
