# https://judge.softuni.org/Contests/Compete/Index/2415#1
x = str(input().lower())

if x == 'monday' or x == 'tuesday'\
or x == 'wednesday' or x == 'thursday'\
or x == 'friday':
    print('Working day')
elif x == 'saturday' or x == 'sunday':
    print('Weekend')
else:
    print('Error')