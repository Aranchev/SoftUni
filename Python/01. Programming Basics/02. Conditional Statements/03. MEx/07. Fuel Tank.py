# https://judge.softuni.org/Contests/Practice/Index/1658#6

a = str(input().lower())
A = float(input())

if a == 'diesel' or a == 'gasoline' or a == 'gas':
    if A >= 25:
        print(f'You have enough {a}.')
    elif A < 25:
        print(f'Fill your tank with {a}!')
else:
    print('Invalid fuel!')

