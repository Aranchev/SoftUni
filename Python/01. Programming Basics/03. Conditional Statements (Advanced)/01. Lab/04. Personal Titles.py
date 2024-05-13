# https://judge.softuni.org/Contests/Compete/Index/2415#3
x = float(input())
y = str(input().lower())

if x >= 16 and y == 'm':
    print('Mr.')
elif x < 16 and y == 'm':
    print('Master')
elif x >= 16 and y == 'f':
    print('Ms.')
elif x < 16 and y == 'f':
    print('Miss')