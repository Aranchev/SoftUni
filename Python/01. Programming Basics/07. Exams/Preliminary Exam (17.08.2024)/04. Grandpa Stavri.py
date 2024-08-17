a = int(input())
b = 0
c = 0
e = 0
for i in range(a):
    b = float(input())
    c += float(input()) * b
    e += b


print(f'Liter: {e:.2f}')
print(f'Degrees: {c/e:.2f}')

if c / e > 42:
    print('Dilution with distilled water!')
elif c / e < 38:
    print('Not good, you should baking!')
else:
    print('Super!')
