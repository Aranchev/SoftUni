import math
a = int(input())
b = int(input())
c = int(input())

for A in range(1, a + 1):
    if A % 2 == 0:
        for B in range(2, b+1):
            a = True
            for i in range(2, int(math.sqrt(B)) + 1):
                if B % i == 0:
                    a = False
                    break
            if a:
                for C in range(1, c+1):
                    if C % 2 == 0:
                        print(A, B, C)
