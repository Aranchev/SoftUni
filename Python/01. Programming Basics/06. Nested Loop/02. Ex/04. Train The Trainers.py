a = int(input()) 
b = input() 
c = 0  
d = 0 
e = 0

while b != 'Finish':
    for i in range(a):
        d += 1
        c += float(input())
    print(f'{b} - {c/a:.2f}.')
    e += c
    c = 0
    b = input()
    
print(f"Student's final assessment is {e/d:.2f}.")
