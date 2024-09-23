a = int(input())

for i in range(97, 97 + a):
    for x in range(97, 97 + a):
        for y in range(97, 97 + a):
            print(f'{chr(i)}{chr(x)}{chr(y)}')
