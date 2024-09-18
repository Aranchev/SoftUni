a = input()
b = ''

for i in a:
    if not i == ',':
        b += f'{i}'

c = b.split(' ')

if c[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for x, y in enumerate(reversed(c), 1):
        if y == 'wolf':
            print(f'Oi! Sheep number {x - 1}! You are about to be eaten by a wolf!')
