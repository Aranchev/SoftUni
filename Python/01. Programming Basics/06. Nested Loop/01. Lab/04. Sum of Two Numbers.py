a = int(input())
b = int(input())
c = int(input())
e = 0



for i in range(a, b+1):
    for x in range(a, b+1):
        e += 1
        if i+x == c:
            break
    else:
        continue
    break

if i + x == c:
    print(f"Combination N:{e} ({i} + {x} = {c})")
else:
    print(f'{e} combinations - neither equals {c}')
