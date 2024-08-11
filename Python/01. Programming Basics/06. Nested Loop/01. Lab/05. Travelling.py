while True:
    c = 0
    a = input()

    if a == 'End':
        break

    b = float(input())

    while True:
        c += float(input())
        if c >= b:
            print(f'Going to {a}!')
            break
