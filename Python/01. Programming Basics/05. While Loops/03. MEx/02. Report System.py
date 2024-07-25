a = int(input())
b = input()
c = 0  # редуване - брой, с карта
d = 0  # плащания в брой
e = 0  # плащания с карта
f = 0  # сума в брой
g = 0  # сума с карта

while b != 'End':
    b = int(b)
    c += 1

    if c % 2 != 0 and b <= 100:
        f += b
        d += 1
        print('Product sold!')
    elif c % 2 == 0 and b >= 10:  # карта
        g += b
        e += 1
        print('Product sold!')
    else:
        print('Error in transaction!')

    if f + g >= a:
        print(f'Average CS: {f / d:.2f}')
        print(f'Average CC: {g / e:.2f}')
        break

    b = input()

if b == 'End' and f + g < a:
    print('Failed to collect required money for charity.')
