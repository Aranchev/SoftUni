import itertools

a = int(input())
b = int(input())

for A, B, C, D in itertools.product(range(a, b + 1), range(a, b + 1), range(a, b + 1), range(a, b + 1)):
    if (
        ((A % 2 == 0 and D % 2 != 0) or (A % 2 != 0 and D % 2 == 0))
        and
        (A > D)
        and
        (B + C) % 2 == 0
    ):
        print(f'{A}{B}{C}{D}', end=' ')
