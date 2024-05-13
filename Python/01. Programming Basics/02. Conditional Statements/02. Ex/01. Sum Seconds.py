# https://judge.softuni.org/Contests/Compete/Index/2414#0
import math
a = int(input())
b = int(input())
c = int(input())
abc = a + b + c  
min = abc // 60  #! колко пъти сумата (abc) влиза в 'знаменателя'
sec = abc % 60  #! остатъка на сумата, след като се раздели на 60
min = math.floor(min) #! Закръглете получената стойност за минутите надолу, за да премахнете дробната част от стойността.
if sec < 10: 
    print(f'{min}:0{sec}')
else:
    print(f'{min}:{sec}')