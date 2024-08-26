a = int(input())
b = int(input())
c = int(input()) 
d = int(input())

for A in range(a + 1):
    for B in range(b + 1):
        for C in range(c + 1):
            if A * 1 + B * 2 + C * 5 == d:
                print(f'{A} * 1 lv. + {B} * 2 lv. + {C} * 5 lv. = {d} lv.')
