# https://judge.softuni.org/Contests/Compete/Index/2415#7
y = str(input().lower())

if y == 'monday':
    f = 12
if y == 'tuesday':
    f = 12
if y == 'wednesday':
    f = 14
if y == 'thursday':
    f = 14
if y == 'friday':
    f = 12
if y == 'saturday':
    f = 16
if y == 'sunday':
    f = 16
print(f)