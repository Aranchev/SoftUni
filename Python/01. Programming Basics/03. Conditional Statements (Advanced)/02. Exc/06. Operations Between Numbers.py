# https://judge.softuni.org/Contests/Compete/Index/2416#5
a = int(input())
b = int(input())
c = str(input())

if c == '+':
    d = a + b
    if d % 2 == 0:
        print(f'{a} {c} {b} = {d} - even')
    else:
        print(f'{a} {c} {b} = {d} - odd')

elif c == '-':
    d = a - b
    if d % 2 == 0:
        print(f'{a} {c} {b} = {d} - even')
    else:
        print(f'{a} {c} {b} = {d} - odd')

elif c == '*':
    d = a * b
    if d % 2 == 0:
        print(f'{a} {c} {b} = {d} - even')
    else:
        print(f'{a} {c} {b} = {d} - odd')
elif c == '/':
    if b != 0:
        d = a / b
        print(f'{a} {c} {b} = {d:.2f}')
    else:
        print(f'Cannot divide {a} by zero')

elif c == '%':
    if b != 0:
        d = a % b
        print(f'{a} {c} {b} = {d}')
    else:
        print(f'Cannot divide {a} by zero')
