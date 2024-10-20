energy = 100
coins = 100
a = input().split('|')
c = True 
for i in a:
    b = i.split('-')

    if b[0] == 'rest':
        if int(b[1]) + energy >= 100:
            print(f'You gained {100 - energy} energy.')
            energy = 100
            print(f'Current energy: 100.') 
        else:
            energy += int(b[1])
            print(f'You gained {b[1]} energy.')
            print(f'Current energy: {energy}.')
        
    elif b[0] == 'order':
        if energy >= 30:
            energy -= 30
            print(f'You earned {b[1]} coins.')
            
            coins += int(b[1])
        else:
            energy += 50
            print(f'You had to rest!')
        
    else:
        if coins >= int(b[1]):
            coins -= int(b[1])
            print(f'You bought {b[0]}.')
        else:
            print(f'Closed! Cannot afford {b[0]}.')
            c = False 
            break
if c:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')
