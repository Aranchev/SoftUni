# https://judge.softuni.org/Contests/Compete/Index/2414#1
a = int(input())
bonus = 0
if a <= 100:
    bonus = 5
elif a > 100 and a <=1000:
    bonus = a * 0.2
elif a > 1000:
    bonus = a * 0.1
if a % 2 == 0:
    bonus += 1
if a % 10 == 5:
    bonus += 2
print(bonus)
print(bonus + a)
