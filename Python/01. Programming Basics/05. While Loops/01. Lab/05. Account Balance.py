a = 0
b = input()

while b != "NoMoreMoney":
    c = float(b)
    if c < 0:
        print("Invalid operation!")
        break
    a += c
    print(f"Increase: {c:.2f}")

    b = input()

print(f"Total: {a:.2f}")
