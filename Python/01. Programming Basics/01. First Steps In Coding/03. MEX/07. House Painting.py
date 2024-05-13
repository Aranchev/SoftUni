# https://judge.softuni.org/Contests/Practice/Index/1642#6
x = float(input()) # вис на къщата
y = float(input()) # дълж на странична стена
h = float(input()) # вис на триъгълната стена на покрива

# пред и зад стена
a = (2 *(x ** 2)) - 2.4      # m

# стран стени
c = (2 * (x * y)) - 4.50

# покрив
tri = 2 * (1/2 * x * h)
prav = 2 * (x * y)

s = (c + a) / 3.4
z = (tri + prav) / 4.3

print(f'{s:.2f}')
print(f'{z:.2f}')
