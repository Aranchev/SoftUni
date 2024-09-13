a = int(input())
b = int(input())

for i in range(1, b + 1):
    if i % a == 0 and i <= b:
        o = i
print(o)
