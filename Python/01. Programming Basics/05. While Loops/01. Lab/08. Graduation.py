a = 1
b = input()
c = 0
e = 0

while a <= 12:
    f = float(input())
    if f < 4:
        if c > 0:
            break  # terminates the loop
        c += 1
        continue  # procedes to the next iteration
    e += f
    a += 1
if a > 12:
    print(f"{b} graduated. Average grade: {e / 12:.2f}")
else:
    print(f"{b} has been excluded at {a} grade")
