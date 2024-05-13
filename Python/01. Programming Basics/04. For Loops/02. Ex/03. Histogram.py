# https://judge.softuni.org/Contests/Compete/Index/2418#2

a = int(input())

c = 0
d = 0
e = 0
f = 0
g = 0

for i in range(a):
    b = int(input())
    if b not in range(1, 1001):
        break
    if b < 200:
        c += 1
    elif b >= 200 and b <= 399:
        d += 1
    elif b >= 400 and b <= 599:
        e += 1
    elif b >= 600 and b <= 799:
        f += 1
    elif b >= 800:
        g += 1

print(f'{c / a * 100:.2f}%')
print(f'{d / a * 100:.2f}%')
print(f'{e / a * 100:.2f}%')
print(f'{f / a * 100:.2f}%')
print(f'{g / a * 100:.2f}%')

