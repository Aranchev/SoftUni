a = int(input())
b = int(input())
c = 0
for A in range(1, a + 1):
    e = 0
    for B in range(1, b + 1):
        if A % 2 == 0 and B % 2 != 0:
            e += 2.50
        elif A % 2 != 0 and B % 2 == 0:
            e += 1.25
        else:
            e += 1
    print(f'Day: {A} - {e:.2f} leva')
    c += e

print(f'Total: {c:.2f} leva')
