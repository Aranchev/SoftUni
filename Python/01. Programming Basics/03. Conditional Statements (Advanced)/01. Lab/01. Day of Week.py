# https://judge.softuni.org/Contests/Compete/Index/2415#0
x = int(input())

if x >= 1 and x <= 7:
    if x == 1:
        print('Monday')
    elif x == 2:
        print('Tuesday')
    elif x == 3:
        print('Wednesday')
    elif x == 4:
        print('Thursday')
    elif x == 5:
        print('Friday')
    elif x == 6:
        print('Saturday')
    elif x == 7:
        print('Sunday')
else:
    print('Error')