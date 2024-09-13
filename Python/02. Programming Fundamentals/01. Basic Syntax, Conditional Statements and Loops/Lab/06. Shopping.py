budget = int(input())
price = input()

while price != 'End':
    price = int(price)
    budget -= price
    if budget < 0:
        break
    price = input()

if budget >= 0:
    print('You bought everything needed.')
elif budget < 0:
    print('You went in overdraft!')
