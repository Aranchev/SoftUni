'''
see here why you've got runtime error: https://chatgpt.com/c/66f85332-9f1c-800e-a5c8-91e9b5bb7249

u used: str.split(), enumerate(), len(), join()
'''
a = input()
b = input()
c = a.split(' ')

while b != 'No Money':
    e = b.split(' ')

    if e[0] == 'OutOfStock':
        for i, n in enumerate(c):
            if n == e[1]:
                c[i] = None
    elif e[0] == 'Required':
        for i, n in enumerate(c):
            if i == int(e[2]):
                c[i] = e[1]
    elif e[0] == 'JustInCase':
        if len(c) > 0:  # Check if the list is not empty
            c[-1] = e[1]
        
    b = input()

new_list = []

for i in c:
    if i is not None:
        new_list.append(i)
c = new_list
o = ' '.join(c)

print(o)

'''
used: split(), join(), replace(), map(), remove()
k1lgor's:
gifts = input().split(' ')

command = input().split(' ')

while command[0] != 'No' and command[1] != 'Money':
    index = 0
    if command[0] == 'OutOfStock':
        gift = command[1]
        gifts = ' '.join(map(str, gifts))
        gifts = gifts.replace(gift, 'None')
        gifts = gifts.split(' ')
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 < index < len(gifts):
            gifts[index] = command[1]
    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]
    
    command = input().split(' ')
    
while 'None' in gifts:
    gifts.remove('None')
    
print(' '.join(map(str, gifts)))
'''
