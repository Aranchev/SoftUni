# https://judge.softuni.org/Contests/Practice/Index/1642#5
a_ = float(input())   # скум - цена/кг
b_ = float(input())   # цаца - цена/кг

c = float(input())    # паламуд - кг
c_ = a_ + (a_ * 0.6)    # паламуд - цена/кг

d = float(input())    # сафрид - кг
d_ = b_ + (b_ * 0.8)  # сафрид - цена/кг

e = int(input())      # миди - кг
e_ = 7.50             # цена/кг

s = (e * e_) + (d * d_) + (c * c_)

print(f'{s:.2f}')
