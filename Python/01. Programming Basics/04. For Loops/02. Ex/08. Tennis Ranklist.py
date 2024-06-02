import math
a = int(input())  #! брой турнири, в които е участвал
b = int(input())  #! начален брой в ранглистата
d = 0
g = 0
for i in range(a):
    c = str(input())
    if c == "W":
        d += 2000
        g += 1
    elif c == "F":
        d += 1200
    elif c == "SF":
        d += 720
e = b + d  #! точки след турнира
f = d / a  #! средно спечели точки за турнир
j = g / a * 100

print(f"Final points: {abs(e)}")  
#! abs returns the absolute value of number

print(f"Average points: {math.floor(f)}") 
#! floor() - Returns the largest integer less than or equal to

print(f"{j:.2f}%")  
#! string formating

