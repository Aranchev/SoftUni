a = int(input())
b = int(input())

c = 0
d = 0

c = a
d = b

print(f'Before:')
print(f'a = {c}\nb = {d}')

c = b
d = a
print('After:')
print(f'a = {c}\nb = {d}')
