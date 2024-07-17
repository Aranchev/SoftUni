a = 10000
b = ''
c = 0

while b != 'Going home':
    b = input()

    if b == 'Going home':
        b = input()
        c += int(b)
        if c >= a:
            print(f'Goal reached! Good job!\n{abs(c - a)} steps over the goal!')
        else:
            print(f'{a - c} more steps to reach goal.')
        break

    c += int(b)

    if c >= a:
        print(
            f'Goal reached! Good job!\n{abs(c - a)} steps over the goal!')
        break
