a = int(input())
b = ''
c = ''
d = ''
e = 0
while b != 'closed':
    if b == 'haircut':
        c = input()
        if c == 'mens':
            e += 15
        elif c == 'ladies':
            e += 20
        elif c == 'kids':
            e += 10

    elif b == 'color':
        d = input()
        if d == 'touch up':
            e += 20
        elif d == 'full color':
            e += 30
    if e >= a:
       print('You have reached your target for the day!')
       print(f'Earned money: {e}lv.')
       break
    
    b = input()

if e < a:
    print(f'Target not reached! You need {a - e}lv. more.\nEarned money: {e}lv.')
