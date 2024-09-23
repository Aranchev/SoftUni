a = int(input())
f = 0
x, y, z = 0, 0, 0
for i in range(a):
    b = int(input()) # weight 
    c = int(input()) # time
    d = int(input()) # quality
    e = (b / c) ** d
    if e >= f:
        f = e
        x, y, z = b, c, d
print(f'{x} : {y} = {int(f)} ({z})')

