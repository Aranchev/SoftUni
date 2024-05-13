# https://judge.softuni.org/Contests/Compete/Index/2417#8
a = int(input())
f = 0
g = 0
for i in range(a):
    c = int(input())
    f += c
for i in range(a):
    e = int(input())
    g += e

if f == g:
    print(f'Yes, sum = {f}')
elif f > g:
    print(f'No, diff = {f - g}')
elif g > f:
    print(f'No, diff = {g - f}')


