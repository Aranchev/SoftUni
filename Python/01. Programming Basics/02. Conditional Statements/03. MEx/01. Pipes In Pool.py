# https://judge.softuni.org/Contests/Practice/Index/1658#0
V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

x = P1 * H
y = P2 * H
z = x + y

if z <= V:
    x_per = x / z * 100
    y_per = y / z * 100
    z_per = z / V * 100
    print(f"The pool is {z_per:.2f}% full. Pipe 1: {x_per:.2f}%. Pipe 2: {y_per:.2f}%.")
else:
    print(f"For {H} hours the pool overflows with {(z - V):.2f} liters.")


