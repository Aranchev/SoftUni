# https://judge.softuni.org/Contests/Practice/Index/1642#9

x = float(input())
if x >= 26.00 and x <= 35.00:
    print('Hot')
elif x >= 20.1 and x <= 25.9:
    print('Warm')
elif x >= 15.00 and x <= 20.00:
    print('Mild')
elif x >= 12.00 and x <= 14.9:
    print('Cool')
elif x >= 5.00 and x <= 11.9:
    print('Cold')
else:
    print('unknown')