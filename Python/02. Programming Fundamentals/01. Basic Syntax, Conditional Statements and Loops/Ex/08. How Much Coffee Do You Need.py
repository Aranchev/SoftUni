a = input()
b = 0
while a != 'END':
    if a in ('dog', 'cat', 'coding', 'movie'):
        b += 1
    elif a in ('DOG', 'CAT', 'CODING', 'MOVIE'):
        b += 2
    if b > 5:
        break
    a = input()

if b > 5:
    print('You need extra sleep')
else:
    print(b)
