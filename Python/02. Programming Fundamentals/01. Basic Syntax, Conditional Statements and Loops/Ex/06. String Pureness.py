a = int(input())

for i in range(a):
    b = input()
    for x in b:
        if x == '_' or x == ',' or x == '.':
            print(f'{b} is not pure!')
            break
    else:
        print(f'{b} is pure.')
