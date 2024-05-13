age = int(input()) #! Годините на Лили
wm_price = float(input()) #! Цена на пералнята
pp_toy = int(input()) #! Единична цена на играч

c = 0
e = 0

for i in range(1, age + 1):
    if i % 2 == 0:  #! четните години на Лили
        c += (10 * (i / 2)) - 1
    elif i % 2 != 0:  #! нечетите години на Лили
        e += 1

toys = e * pp_toy
money = c + toys

if money >= wm_price:
    print(f'Yes! {money - wm_price:.2f}')

elif money < wm_price:
    print(f'No! {wm_price - money:.2f}')
