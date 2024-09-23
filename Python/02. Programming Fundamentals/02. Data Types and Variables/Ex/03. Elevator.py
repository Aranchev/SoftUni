a = int(input())
b = int(input())
c = 0

if a <= b:
    c = 1
    print(c)
elif a > b:
    if a % b == 0:
        print(a // b)
    elif a % b != 0:
        print(a // b + 1)
