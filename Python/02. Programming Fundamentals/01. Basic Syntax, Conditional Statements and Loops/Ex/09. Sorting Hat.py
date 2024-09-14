a = input()

while a != 'Welcome!':

    if a == 'Voldemort':
        print('You must not speak of that name!')
        break

    if len(a) < 5:
        print(f'{a} goes to Gryffindor.')
    elif len(a) == 5:
        print(f'{a} goes to Slytherin.')
    elif len(a) == 6:
        print(f'{a} goes to Ravenclaw.')
    elif len(a) > 6:
        print(f'{a} goes to Hufflepuff.')

    a = input()

if a == 'Welcome!':
    print('Welcome to Hogwarts.')
