a = str(input())  #! име на актьора
b = float(input())  #! точки от академията
c = int(input())  #! брой оценяващи

for i in range(c):
    if b >= 1250.5:
        break
    f = str(input())  #! име на оценяващия
    e = float(input())  #! точки от оценяващия
    b += len(f) * e / 2

if b >= 1250.5:
    print(f"Congratulations, {a} got a nominee for leading role with {b:.1f}!")
else:
    print(f"Sorry, {a} you need {1250.5 - b:.1f} more!")
