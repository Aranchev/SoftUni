a = int(input())
c = False
for i in range(a):
    b = int(input())
    if b % 2 == 0:
        continue
    else:
        print(f'{b} is odd!')
        c = True
        break

if not c:
    print('All numbers are even.')
