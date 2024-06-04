a = str(input())  #! име на актьора
b = float(input())  #! точки от академията
c = int(input())  #! брой оценяващи

for i in range(c):
    if b >= 1250.5:
        break
'''
When the break statement is encountered within 
a loop (either a for loop or a while loop), 
the loop is immediately terminated, and the program
control moves to the first statement following the loop.
'''
    f = str(input())  #! име на оценяващия
    e = float(input())  #! точки от оценяващия
    b += len(f) * e / 2

if b >= 1250.5:
    print(f"Congratulations, {a} got a nominee for leading role with {b:.1f}!")
else:
    print(f"Sorry, {a} you need {1250.5 - b:.1f} more!")
