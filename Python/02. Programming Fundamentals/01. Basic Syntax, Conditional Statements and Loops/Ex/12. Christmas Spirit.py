a = int(input()) #! quantity of decorations
b = int(input()) #! days left until Christmas

c, d, e, f = 2, 5, 3, 15  #! dec price/piece
c_p, d_p, e_p, f_p = 5, 3, 10, 17 #! dec spirit/shopping

g = 0   #! money 
h = 0   #! spirit

for i in range(1, b + 1):
    if i % 11 == 0:
        a += 2

    if i % 2 == 0:
        g += a * c
    if i % 3 == 0:
        g += a * d
        g += a * e
    if i % 5 == 0:
        g += a * f

    if i % 10 == 0:
        g += d + e + f
    
   
for i in range(1, b + 1):
    if i % 2 == 0:
        h += c_p
    if i % 3 == 0:
        h += d_p + e_p
    if i % 5 == 0:
        h += f_p

    if i % 5 == 0 and i % 3 == 0:
        h += 30

    if i % 10 == 0:
        h -= 20

if b % 10 == 0:
    h -= 30

print(f'Total cost: {g}')
print(f'Total spirit: {h}')
