a = input().lower()   #! main string
b = 'water'   #! str to be found
b_1 = 'fish'
b_2 = 'sand'
b_3 = 'sun'
c = 0         #! occurrences counter
d = 0         #! start indx

for i in range(len(a)):
    e = a.find(b, d)
    if e != -1:
        d = e + 1
        c += 1
d = 0

for i in range(len(a)):
    f = a.find(b_1, d)
    if f != -1:
        d = f + 1
        c += 1

d = 0

for i in range(len(a)):
    g = a.find(b_2, d)
    if g != -1:
        d = g + 1
        c += 1

d = 0

for i in range(len(a)):
    h = a.find(b_3, d)
    if h != -1:
        d = h + 1
        c += 1


print(c)
