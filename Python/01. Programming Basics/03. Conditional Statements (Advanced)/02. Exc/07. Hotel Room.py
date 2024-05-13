# https://judge.softuni.org/Contests/Compete/Index/2416#6
a = str(input().lower()) # месец
b = int(input())         # брой нощувки

c = 0 # цена за нощувка студио
d = 0 # цена за нощувка апартамент
f = 0 # намаления на апартамент
e = 0 # намаления на студио

if a == 'may' or a == 'october':
    c = 50
    d = 65
    if b > 7:
        e = 0.05    # отстъпка студио
    if b > 14:
        e = 0.3
elif a == 'june' or a == 'september':
    c = 75.20
    d = 68.70
    if b > 14:
        e = 0.2
elif a == 'july' or a == 'august':
    c = 76
    d = 77

g = c * b
g -= g * e
h = d * b

if b > 14:
    h -= h * 0.1

print(f'Apartment: {h:.2f} lv.')
print(f'Studio: {g:.2f} lv.')



