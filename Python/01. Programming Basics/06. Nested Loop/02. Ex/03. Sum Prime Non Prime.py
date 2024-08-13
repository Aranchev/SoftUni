a = input()
b = 0
c = 0

while a != 'stop':
    a = int(a)
    if a >= 0:
        for i in range(2, a):
            if a % i == 0:
                b += a
                break
        else:
            c += a
    else:
        print('Number is negative.')
    a = input()

print(f'Sum of all prime numbers is: {c}')
print(f'Sum of all non prime numbers is: {b}')
