def num_def(a: float):
    if a == 0:
        return 'zero' 
    elif a > 0 and a < 1:
        return 'small positive'
    elif a < 0 and a > -1:
        return 'small negative'
    elif a > 1000000:
        return 'large positive'
    elif a < -1000000:
        return 'large negative'
    elif a >= 1 and a <= 1000000:
        return 'positive'
    elif a <= -1 and a >= -1000000:
        return 'negative'

if __name__ == '__main__':
    d = float(input())
    print(num_def(d))

