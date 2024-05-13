#https://judge.softuni.org/Contests/Compete/Index/2414#2
h = int(input())
m = int(input()) + 15

if m > 59:
    h += 1
    m -= 60
if h > 23:
    h = 0

print(f'{h}:{m:02d}') #! {m:02d} represents the value of the variable m, formatted as a zero-padded two-digit number


