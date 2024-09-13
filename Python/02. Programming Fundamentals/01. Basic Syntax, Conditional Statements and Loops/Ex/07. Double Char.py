a = input()
o = ''
while a != 'End':
    if a == 'SoftUni':
        a = input()
        continue
    for i in a:
        o += i * 2
    print(o)
    o = ''
    a = input()
