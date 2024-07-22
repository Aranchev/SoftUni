a = int(input())
b = int(input())
c = a * b
d = input()

while d != 'STOP':
    d = int(d)
    c -= d

    if c <= 0:
        print(f'No more cake left! You need {abs(c)} pieces more.')
        break

    d = input()

if d == 'STOP':
    print(f'{c} pieces are left.')
