c = int(input())  # брой незадоволителни оценки
a = input()  # string
f = 0
b = 0
g = 0
d = 0
r = ''

while a != 'Enough':
    f = int(input())  # оценка
    b += f  # сума на оценките
    d += 1
    r = a
    if f <= 4:
        g += 1

        if g == c:
            print(f'You need a break, {g} poor grades.')
            break

    a = input()

if a == 'Enough':
    print(f'Average score: {b / d:.2f}')
    print(f'Number of problems: {d}')
    print(f'Last problem: {r}')
