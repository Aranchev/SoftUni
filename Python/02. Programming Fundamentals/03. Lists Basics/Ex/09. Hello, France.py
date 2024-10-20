a = input().split('|')
# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60

b = float(input()) # 120

# print(a) # --> after the first split

x = []

y = ''

z = 0

o = 0

for i in a:
    c = i.split('->')
    # print(c) --> list ['item', 'price']

    if c[0] == 'Clothes':
        if float(c[1]) > 50.00 or float(c[1]) > b:
            continue
        else:
            b -= float(c[1]) 
            x += [float(c[1])]
            z += float(c[1]) * 0.4

    elif c[0] == 'Shoes':
        if float(c[1]) > 35.00 or float(c[1]) > b:
            continue
        else:
            b -= float(c[1])
            x += [float(c[1])] 
            z += float(c[1]) * 0.4

    elif c[0] == 'Accessories':
        if float(c[1]) > 20.50 or float(c[1]) > b:
            continue
        else:
            b -= float(c[1])
            x += [float(c[1])] 
            z += float(c[1]) * 0.4


for i in x:
    print(f'{i + (i * 0.4):.2f}', end=' ')
    
print(f'\nProfit: {z:.2f}')

for i in x:
    o += float(i)
if o + z + b >= 150.00:
    print('Hello, France!')
else:
    print('Not enough money.')
print(y)
