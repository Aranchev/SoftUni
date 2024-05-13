# https://judge.softuni.org/Contests/Compete/Index/2424#8
dylj = int(input())
shir = int(input())
vis = int(input())
proc = float(input()) / 100
x = dylj * shir * vis / 1000
y = x * (1 - proc)
print(y)