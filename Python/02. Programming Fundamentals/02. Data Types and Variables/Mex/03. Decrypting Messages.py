a = int(input())
b = int(input())
f = ''
for i in range(b):
    c = ord(input())
    c += a
    f += f'{chr(c)}'
print(f)
    
