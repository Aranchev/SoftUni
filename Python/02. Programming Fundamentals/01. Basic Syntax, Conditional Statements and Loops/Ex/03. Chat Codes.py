a = int(input())

for i in range(a):
    b = int(input())
    if b == 88:
        print('Hello')
    elif b == 86:
        print('How are you?')
    elif b != 88 and b != 86 and b < 88:
        print('GREAT!')
    elif b > 88:
        print('Bye.')
