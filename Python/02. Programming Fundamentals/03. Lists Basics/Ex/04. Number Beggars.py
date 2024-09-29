#? list.join(), str.split(), list.append(), list.remove(), in, not in
'''
test input:
    a = 1, 2, 3, 4, 5
    b = 2
'''

a = input()
b = int(input())
d = []
f = []
e = []
o = []
g = []
h = 0
# transforming the 'a' string into list of integers
c = a.split(', ')
for i in c:
    d += [int(i)]
# (a) 1, 2, 3, 4, 5 --> [1, 2, 3, 4, 5]

for i in range(b):
    e += [c[i::b]]

for i in e:
    o = []
    for x in i:
        o += [int(x)]
    g += [sum(o)]

print(g)

'''
k1lgor's genious solution

int_string = input()
count = int(input())

string = int_string.split(', ')
sum1 = 0
List = []
for i in range(count):
    beggars = string[i::count]
    for d in beggars:
        sum1 += int(d)
    List.append(sum1)
    sum1 = 0
print(List)
'''
