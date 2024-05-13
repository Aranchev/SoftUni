# https://judge.softuni.org/Contests/Practice/Index/1658#3
A = int(input()) # брой километри
B = str(input().lower()) # дума “day” или “night”
if A < 20:
    if B == "day":
        c = A * 0.79 + 0.70
    if B == "night":
        c = A * 0.90 + 0.70
elif A >= 20 and A < 100:
    c = A * 0.09
elif A >= 100:
    c = A * 0.06
print(f'{c:.2f}')







