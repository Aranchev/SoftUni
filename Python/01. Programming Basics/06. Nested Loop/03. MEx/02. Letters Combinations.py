a = str(input())
b = str(input())
c = str(input())
o = 0

for A in range(ord(a), ord(b) + 1):
    if A != ord(c):
        for B in range(ord(a), ord(b)+1):
            if B != ord(c):
                for C in range(ord(a), ord(b) + 1):
                    if C != ord(c):
                        o += 1
                        print(f'{chr(A)}{chr(B)}{chr(C)}', end=' ')

print(o)
