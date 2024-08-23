a = str(input())
b = int(input())
c = int(input())
d = 0
for A in range(ord('A'), ord(a) + 1):
    for B in range(1, b + 1):
        if B % 2 != 0:
            for C in range(ord('a'), ord('a') + c):
                print(f'{chr(A)}{B}{chr(C)}')
                d += 1
        elif B % 2 == 0:
            for D in range(ord('a'), ord('a') + c + 2):
                print(f'{chr(A)}{B}{chr(D)}')
                d += 1
    b += 1

print(d)
