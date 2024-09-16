a = float(input())  #! budget
b = float(input())  #! price of kg flour
c = b * 0.75        #! price for pack of eggs
d = b * 1.25        #! price for liter of milk
e = d / 4           #! price for quarter of milk
f = b + c + e       #! price for a piece of loaf
g = a // f          #! loaves in budget
h = 0               #! eggs
j = 0               #! some counter 

# print(g * f) # spent money
# print(a - g * f) # rest of money

for i in range(1, int(g) + 1):
    if a < f:
        break
    h += 3
    j += 1
    if j == 3:
        h -= i - 2
        j = 0

print(f'You made {int(g)} loaves of Easter bread! Now you have {int(h)} eggs and {a - g * f:.2f}BGN left.')
