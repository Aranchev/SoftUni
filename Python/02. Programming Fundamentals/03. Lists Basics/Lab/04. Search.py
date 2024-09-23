a = int(input())
b = input()
d = []
e = []
for i in range(a):
    c = input()
    d += [c]
    if b in c:
        e += [c]
    
print(d)
print(e)

# alternative solution with remove() and reverse loop:
'''
a = int(input())
b = input()
c = []

for i in range(a):
    e = input()
    c.append(e)
print(c)

for i in range(len(c) - 1, -1, -1):
    f = c[i]
    if b not in f:
        c.remove(f)
print(c)

'''
