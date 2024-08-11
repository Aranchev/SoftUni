a = int(input())
b = int(input())

for i in range(a, 0, -1):
    if i < a:
        print()
    for i in range(b):
        if i == a:
            print(f'L{i}{i} ', end="")
        elif i % 2 == 0:
            print(f'O{i}{i} ', end="")
        else:
            print(f'A{i}{i} ', end="")
