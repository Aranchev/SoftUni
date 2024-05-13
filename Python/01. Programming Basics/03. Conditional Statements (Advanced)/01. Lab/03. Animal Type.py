# https://judge.softuni.org/Contests/Compete/Index/2415#2
x = str(input().lower())

if x == 'dog':
    print('mammal')
elif x == 'crocodile' or x == 'tortoise'\
or x == 'snake':
    print('reptile')
else:
    print('unknown')