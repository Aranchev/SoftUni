a = str(input())
c = []
e = ''
for i in a:
    c += [int(i)]

c.sort(reverse=True)

for i in c:
    e += f'{i}'

print(e)
