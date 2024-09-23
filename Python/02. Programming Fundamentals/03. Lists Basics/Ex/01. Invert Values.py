# abs(), -abs(), split()

a = input() 
b = a.split(' ')
c = []
for i in b:
    if int(i) < 0:
        c += [abs(int(i))]
    elif int(i) > 0:
        c += [-abs(int(i))]
    else:
        c += [int(i)]
print(c)    
