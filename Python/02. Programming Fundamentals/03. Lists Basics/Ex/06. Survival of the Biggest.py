# ', '.join(map(str, x))
# str.split(), list.remove()
a = input()
b = int(input())
c = a.split(' ')
d = []

for i in c:
    d += [int(i)]


for i in range(b):
    for x in d:
        if x == min(d):
            d.remove(x)
            break

print(', '.join(map(str, d)))

'''
k1lgor's:

new_list = list(map(int, input().split()))
count = int(input())

for _ in range(count):
    new_list.remove(min(new_list))
print(', '.join(map(str, new_list)))

'''
