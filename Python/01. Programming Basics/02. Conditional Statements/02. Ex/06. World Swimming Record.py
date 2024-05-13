a = float(input())
b = float(input())
c = float(input())
# https://judge.softuni.org/Contests/Compete/Index/2414#5
e = b * c 
s = (b // 15) * 12.5 
es = e + s

if a <= es:
    print(f"No, he failed! He was {es - a:.2f} seconds slower.")

if a > es:
    print(f"Yes, he succeeded! The new world record is {es:.2f} seconds.")