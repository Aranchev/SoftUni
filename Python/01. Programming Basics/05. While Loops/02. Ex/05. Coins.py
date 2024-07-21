a = float(input()) * 100
b = 0

while a >= 200:
    a -= 200
    b += 1

while a >= 100:
    a -= 100
    b += 1
    
while a >= 50:
    a -= 50
    b += 1

while a >= 20:
    a -= 20
    b += 1

while a >= 10:
    a -= 10
    b += 1

while a >= 5:
    a -= 5
    b += 1

while a >= 2:
    a -= 2
    b += 1

while a >= 1:
    a -= 1
    b += 1

print(b)
