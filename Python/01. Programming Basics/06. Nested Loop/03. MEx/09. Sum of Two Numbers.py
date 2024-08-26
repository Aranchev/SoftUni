a = int(input())
b = int(input())
c = int(input())
e = 0
f = False

for i in range(a, b + 1):
    for x in range(a, b + 1):
        e += 1
        if i + x == c:
            print(f'Combination N:{e} ({i} + {x} = {i + x})')
            f = True
            
        if f:
            break
    if f:
        break

if not f:
    print(f'{e} combinations - neither equals {c}')
