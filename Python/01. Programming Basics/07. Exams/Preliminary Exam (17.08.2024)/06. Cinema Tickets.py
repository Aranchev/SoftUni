a = input() #! name of movie
h = 0 #! total tickets
j = 0
k = 0
l = 0

while a != 'Finish':
    b = int(input()) #! free spaces
    c = input()      #! billet type
    d = 0 #! student
    e = 0 #! standard
    f = 0 #! kid
    g = 0 #! sum of tickets

    while c != 'End':
        if c == 'student':
            d += 1
        elif c == 'standard':
            e += 1
        elif c == 'kid':
            f += 1
        g = d + e + f
        if g >= b:
            break
        c = input()

    j += d
    k += e
    l += f
    h += g
    print(f'{a} - {g / b * 100:.2f}% full.')
    a = input()

print(f'Total tickets: {h}')
print(f'{j / h * 100:.2f}% student tickets.')
print(f'{k / h * 100:.2f}% standard tickets.')
print(f'{l / h * 100:.2f}% kids tickets.')
