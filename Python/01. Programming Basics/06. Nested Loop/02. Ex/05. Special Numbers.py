a = int(input())
b = 0

for i in range(1111, 9999+1):
    b = 0
    for x in str(i): 
        if int(x) > 0:
            if a % int(x) != 0:
                b += 1
        else:
            b += 1
            break
    if b == 0:
        print(i, end=' ')
