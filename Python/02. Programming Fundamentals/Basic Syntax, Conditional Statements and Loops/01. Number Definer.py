a = float(input())

if a < 1 and a > 0:
    print('small positive')
elif a < 0 and a > -1:
    print('small negative')
elif a > 1000000:
    print('large positive')
elif a < -1000000:
    print('large negative')
elif a > 0:
    print('positive')
elif a < 0:
    print('negative')
elif a == 0:
    print('zero')
