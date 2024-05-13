# https://judge.softuni.org/Contests/Compete/Index/2424#4
pen = float(input()) * 5.80
marker = float(input()) * 7.20
prep = float(input()) * 1.20
nam = (float(input()) / 100) * (pen + marker + prep)
res = (pen + marker + prep) - nam
print(res)