a = input()
c = int(input())
d = a.split(' ')
g = []

while True:
    g = []
    c -= 1

    e = d[:int(len(d) / 2)]
    f = d[int(len(d) / 2):]

    for i in range(len(e)):
        g += [e[i]]
        g += [f[i]]
    
    d = g

    if c == 0:
        print(g)
        break

'''
k1lgor's solution:
new function called zip() is used:

string = input().split(' ')
shuffle = int(input())
shuffled = []

for _ in range(shuffle):
    half1 = string[:len(string)//2]
    half2 = string[len(string)//2:]

    for j in zip(half1, half2):
        shuffled.extend(j)
    string = shuffled
    shuffled = []

print(string)
'''
