a = int(input())

for i in range(1, a + 1):
    b = 0
    for x in str(i):
        b += int(x)    
    if b == 7 or b == 5 or b == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
