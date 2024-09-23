a = int(input())
b = True
for i in range(1, a + 1):
    if i > 1 and i < a and a % i == 0:
        b = False
print(b)
      
