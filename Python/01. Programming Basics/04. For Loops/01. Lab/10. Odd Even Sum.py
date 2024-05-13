# https://judge.softuni.org/Contests/Compete/Index/2417#9
'''
да се напише програма, която чете n-на брой цели числа, подадени от потребителя
и проверява дали сумата от числата на четни позиции е равна на сумата на числата
на нечетни позиции
ако да: 'Yes' и на нов ред f'Sum = {сумата}'
не: 'No', f'Diff = {разликата}
разликата се изчислява по абсолютна стойност
'''

a = int(input())
c=0
d=0
for i in range(1, a+1): #! този формат на range() дава възможност да започнеш от 1, а не от 0 и количеството на range() (като сума числа) да се запази
    b = int(input())
    if i % 2 == 0:
        c+=b
    elif i % 2 != 0:
        d+=b 

if c == d:
    print(f'Yes\nSum = {d}')
elif c != d:
    print(f'No\nDiff = {abs(c-d)}')