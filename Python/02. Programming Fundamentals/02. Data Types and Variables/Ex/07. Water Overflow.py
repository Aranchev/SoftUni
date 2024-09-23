a = int(input())
b = 255
c = 0

for i in range(a):
    d = int(input())
    c += d
    if c > b:
        c -= d
        print('Insufficient capacity!')
print(c)
