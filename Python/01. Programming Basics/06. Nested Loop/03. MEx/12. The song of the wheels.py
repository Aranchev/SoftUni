M = int(input())
e = 0
o = 0
for a in range(1, 10):
    for b in range(1, 10):
        if a < b:
            for c in range(1, 10):
                for d in range(1, 10):
                    if c > d:
                        if a * b + c * d == M:
                            e += 1
                            f = f'{a}{b}{c}{d}'
                            print(f'{f} ', end='')
                            if e == 4:
                                o = f'{a}{b}{c}{d}'
if e >= 4:
    print(f'\nPassword: {o}',)
else:
    print('\nNo!')

# k1lgor's solution https://github.com/k1lgor/SoftUni/blob/main/Python%20Basics/Nested%20Loops/More%20Exercises/the_song_of_the_wheels.py
