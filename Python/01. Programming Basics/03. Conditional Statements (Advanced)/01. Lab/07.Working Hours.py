# https://judge.softuni.org/Contests/Compete/Index/2415#6
x = int(input())
y = str(input().lower())

if x >= 10 and x <= 18 and\
(y == 'monday' or y == 'tuesday' or
y == 'wednesday' or y == 'thursday'
or y == 'friday' or y == 'saturday'):
    print('open')
else:
    print('closed')

    