tail = input()
body = input()
head = input()

a = [tail, body, head]

a[0], a[2] = a[2], a[0]

print(a)
