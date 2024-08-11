n = int(input())
b = 1
c = False
for d in range(1, n + 1):
    for _ in range(1, d + 1):
        if b > n:
            c = True
            break
        print(f'{b} ', end='')
        b += 1
    if c:
        break
    print()
