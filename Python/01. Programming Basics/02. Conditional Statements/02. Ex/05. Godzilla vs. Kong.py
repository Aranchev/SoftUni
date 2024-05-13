# https://judge.softuni.org/Contests/Compete/Index/2414#4
budget = float(input())
num_statists = int(input())
price_of_clothing = float(input()) * num_statists

dekor = budget * 0.1

if num_statists > 150: #? the price of clothing calculation should be right
    discount = price_of_clothing * 0.1
    price_of_clothing = price_of_clothing - discount  

x = dekor + price_of_clothing

if x > budget:
    deficit = x - budget
    print(f'Not enough money!\nWingard needs {deficit:.2f} leva more.')

if x <= budget:
    plus = budget - x
    print(f"Action!\nWingard starts filming with {plus:.2f} leva left.")