a = input()
b = 1  #
c = 0
f = 0


while b <= 12:  #
    e = float(input())  #
    if e >= 4:
        f += e
        b += 1
    elif e < 4:
        c += 1
        if c > 1:
            break
if b > 12:
    print(f'{a} graduated. Average grade: {f / 12:.2f}')
else:
    print(f'{a} has been excluded at {b} grade')
