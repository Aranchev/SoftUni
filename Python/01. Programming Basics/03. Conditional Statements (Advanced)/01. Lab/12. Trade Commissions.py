# https://judge.softuni.org/Contests/Compete/Index/2415#11
A = str(input()).lower() # град (текст)
B = float(input())       # обем на продажби
C = 0

if A == 'sofia':
    if B >= 0 and B <= 500:
        C = 0.05
        c = B * C
    elif B > 500 and B <= 1000:
        C = 0.07
        c = B * C
    elif B > 1000 and B <= 10000:
        C = 0.08
        c = B * C
    elif B > 10000:
        C = 0.12
        c = B * C


elif A == 'varna':
    if B >= 0 and B <= 500:
        C = 0.045
        c = B * C
    elif B > 500 and B <= 1000:
        C = 0.075
        c = B * C
    elif B > 1000 and B <= 10000:
        C = 0.1
        c = B * C
    elif B > 10000:
        C = 0.13
        c = B * C


elif A == 'plovdiv':
    if B >= 0 and B <= 500:
        C = 0.055
        c = B * C
    elif B > 500 and B <= 1000:
        C = 0.08
        c = B * C
    elif B > 1000 and B <= 10000:
        C = 0.12
        c = B * C
    elif B > 10000:
        C = 0.145
        c = B * C


if (A == 'sofia' or A == 'varna' or A == 'plovdiv') and B > 0:
    print(f'{c:.2f}')
else:
    print('error')