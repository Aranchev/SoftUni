a = int(input())
b = int(input())
c = int(input())
d = a * b * c
f = input()
g = 0
while f != 'Done':
    f = int(f)
    g += f
    if g >= d:
        print(f'No more free space! You need {g - d} Cubic meters more.')
        break
    f = input()
if f == 'Done':
    print(f'{d - g} Cubic meters left.')
