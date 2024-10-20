a = input().split('#') # fires with their cells
b = int(input())       # water
d = 0                  # total fire            
e = 0                  # effort
f = f'Cells:'

for i in a:
    c = i.split(' ')
   
    if b < int(c[2]):
        continue

    if c[0] == 'High':
        if 81 <= int(c[2]) <= 125:
            b -= int(c[2])
            d += int(c[2])
            f += f'\n- {int(c[2])}'
    
    elif c[0] == 'Medium':
        if 51 <= int(c[2]) <= 80:
            b -= int(c[2])
            d += int(c[2])
            f += f'\n- {int(c[2])}'
    
    elif c[0] == 'Low':
        if 1 <= int(c[2]) <= 50:
            b -= int(c[2])
            d += int(c[2])
            f += f'\n- {int(c[2])}'

e += d * 0.25
print(f)
print(f'Effort: {e:.2f}')
print(f'Total Fire: {d}')
