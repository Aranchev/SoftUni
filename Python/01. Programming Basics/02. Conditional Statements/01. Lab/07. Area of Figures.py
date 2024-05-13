# https://judge.softuni.org/Contests/Compete/Index/2413#6
from math import pi
vid = str(input())
if vid == 'square':
    size = float(input())
    S = size ** 2
    print(f'{S:.3f}')  # f'...': This is an f-string, a feature
elif vid == 'rectangle':  # that allows you to embed expressions inside string literals using curly braces {}.
    sizea = float(input())  # The f before the opening quote indicates that this is an f-string.
    sizeb = float(input())  # '{S:.3f}': This is the expression inside the f-string. Here, 'S' is a variable that holds a
    S = sizea * sizeb  # floating-point number. The ':.3f' is called a format specifier, and it tells Python how to
    print(f'{S:.3f}')  # format the number. The '.' separates the integer and fractional parts of the number, and the '3f'
elif vid == 'circle':  # specifies that there should be three digits after the decimal point.
    r = float(input())  # the colon (':') is used as part of a format specifier to specify the format of the value being printed.
    S = pi * r ** 2     # So, overall, print(f'{S:.3f}') will print the value of S with three digits after the decimal point.
    print(f'{S:.3f}')
elif vid == 'triangle':
    b = float(input())
    h = float(input())
    S = 1/2 * b * h
    print(f'{S:.3f}')
