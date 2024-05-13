# https://judge.softuni.org/Contests/Compete/Index/2414#3
a = float(input()) # цена на екскурзията
b = int(input())   # бр. пъзели 
c = int(input())   # бр. говорещи кукли 
d = int(input())   # бр. плюшени мечета 
e = int(input())   # бр. миньони 
f = int(input())   # бр. камьони 

b_c = 2.60
c_c = 3
d_c = 4.10
e_c = 8.20
f_c = 2

br = b + c + d + e + f

m = (b * b_c) + (c * c_c) + (d * d_c) + (e * e_c) + (f * f_c)

if br >= 50:
    m = m - (m * 0.25)

nm = (m * 0.1)

mng = m - nm

if a > mng:
    x = a - mng
    print(f'Not enough money! {x:.2f} lv needed.')
elif a <= mng:
    y = mng - a
    print(f'Yes! {y:.2f} lv left.')