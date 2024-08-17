n = int(input())
o = False
count = 0
for a in range(1, 9 + 1):
    for b in range(9, a, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c, -1):
                num_sum = a + b + c + d
                num_mult = a * b * c * d
                if num_sum == num_mult and n % 10 == 5:
                    count += 1
                    print(f'{a}{b}{c}{d}')
                    o = True
                    break
                elif num_mult // num_sum == 3 and n % 3 == 0:
                    count += 1
                    print(f'{d}{c}{b}{a}')
                    o = True
                    break
            if o:
                break
        if o:
            break
    if o:
        break
if count == 0:
    print("Nothing found")
