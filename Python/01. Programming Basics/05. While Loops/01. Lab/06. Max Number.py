import sys
a = input() 
b = -sys.maxsize

while a != 'Stop':
    c = int(a)
    if c >= b:
        b = c
    a = input()
    
print(b)
