a = int(input())
o = 0

for i in range(a):
    b = float(input())
    c = int(input())
    d = int(input())
    if b >= 0.01 and b <= 100.00 and c >= 1 and c <= 31 and d  >= 1 and d <= 2000:
        print(f'The price for the coffee is: ${b * c * d:.2f}')

        o += b * c * d
print(f'Total: ${o:.2f}')
