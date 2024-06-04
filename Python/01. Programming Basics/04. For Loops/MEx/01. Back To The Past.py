a = float(input())
b = int(input())
c = a + 0
for i in range((b+1) - 1800):
    if i % 2 == 0:
        a -= 12000
    elif i % 2 != 0:
        a -= 12000 + 50 * (18 + i)

if a >= 0:
    print(f"Yes! He will live a carefree life and will have {a:.2f} dollars left.")
else:
    print(f"He will need {abs(a):.2f} dollars to survive.")
