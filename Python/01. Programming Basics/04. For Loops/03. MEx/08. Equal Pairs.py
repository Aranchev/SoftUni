a = int(input())                    # Това е стойността, която влиза в range() (Input №1)'''
b = int(input()) + int(input())     # Това са инпут №2 и №3 

c = 0                               # Това е разковничето, променливата, в която ще се окаже разликата между двойките числа   

for i in range(a - 1):               # цикълът се завърта а-1 пъти
    d = int(input()) + int(input())    # инпут №3 и №4 * а-1
    if abs(b - d) > c:                 # ако абсолютната стойност на (b - d) > c, което е равно на 0,...
        c = abs(b - d)                   # ..., то 'c' = на въпросната стойност. С други думи: ако b-d > 0
    b = d                              # b присвоява стойността на d. С др думи ако b-d > 0, b присвоява стойността на d
if c == 0:                           # ako в крайна сметка c си остава 0, то това означава, че всички двойки са равни
    print(f"Yes, value={b}")
else:                                # ли не, разликата се крие в 'c'
    print(f"No, maxdiff={c}")
