# https://judge.softuni.org/Contests/Compete/Index/2416#0
a = str(input().lower())
b = int(input())
c = int(input())

if a == 'premiere':
    e = (b * c) * 12
elif a == 'normal':
    e = (b * c) * 7.50
elif a == 'discount':
    e = (b * c) * 5
print(f'{e:.2f} leva.')
