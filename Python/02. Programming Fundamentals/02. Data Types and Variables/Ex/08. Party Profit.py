a = int(input()) # group size
b = int(input()) # days
c = 0

for i in range(1, b + 1):
    if i % 10 == 0:
        a -= 2
    if i % 15 == 0:
        a += 5
    c += 50
    c -= a * 2
    if i % 3 == 0:
        c -= a * 3
    if i % 5 == 0:
        c += a * 20
    if i % 5 == 0 and i % 3 == 0:
        c -= a * 2

print(f'{a} companions received {int((c / a))} coins each.')
