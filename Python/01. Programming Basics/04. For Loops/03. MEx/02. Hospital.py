a = int(input())
b = 0  #! прегледани
c = 0  #! непрегледани
f = 7

for i in range(1, a + 1):  #! 1-4 
    d = int(input())  #! брой пациенти

    if d <= f:
        b += d

    if i % 3 == 0 and c > b:
        f += 1

    if d > f:
        b += f
        c += d - f
        


print(f"Treated patients: {b}.")
print(f"Untreated patients: {c}.")
