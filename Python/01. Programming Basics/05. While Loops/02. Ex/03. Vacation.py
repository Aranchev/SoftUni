a = float(input())
b = float(input())
c = 0
d = 0

while b < a and d < 5:
    e = input()
    f = float(input())
    c += 1

    if e == 'save':
        b += f
        d = 0
    elif e == 'spend':
        b -= f
        d += 1
        if b < 0:
            b = 0

if d == 5:
    print('You can\'t save the money.')
    print(c)
if b >= a:
    print(f'You saved the money for {c} days.')
