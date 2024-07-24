a = int(input()) * 750
b = input()
c = 0
d = 0
f = 0
while b != 'End':
    b = int(b)
    c += 1

    if c % 3 == 0:
        a -= b * 15
        d += b
    else:
        a -= b * 5
        f += b
    if a < 0:
        print(f'Not enough detergent, {abs(a)} ml. more necessary!')
        break

    b = input()

if b == 'End':
    print(f'Detergent was enough!\n {f} dishes and {d} pots were washed.\n Leftover detergent {a} ml.')
