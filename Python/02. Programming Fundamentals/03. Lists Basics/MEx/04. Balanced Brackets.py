# не успях да се справя със тази задача, а остроумното решение идва от https://softuni.bg/forum/37967/5-balanced-brackets-python#answer-64868 

a = int(input())

b = True
c = ''
for _ in range(0, a):
    d = input()
    if d not in ['(', ')']:
        continue

    if c == '' and d == ')' or c == d:
        b = False
        break

    c = d

if b:
    print('BALANCED')
else:
    print('UNBALANCED')
