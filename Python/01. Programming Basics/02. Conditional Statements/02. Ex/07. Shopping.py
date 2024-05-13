# https://judge.softuni.org/Contests/Compete/Index/2414#6
budget = float(input())
n_vc = int(input())
n_p = int(input())
n_r = int(input())

vc = 250 * n_vc
p = (vc * 0.35) * n_p
r = (vc * 0.1) * n_r

x = vc + p + r

if n_vc > n_p:
    x = x - (x * 0.15)

if x <= budget:
    print(f"You have {budget - x:.2f} leva left!")

elif x > budget: 
    print(f"Not enough money! You need {x - budget:.2f} leva more!")