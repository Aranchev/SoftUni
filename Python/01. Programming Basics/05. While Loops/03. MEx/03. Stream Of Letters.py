a = ''
b = ''
c = False
o = False
n = False
f = ''
g = " "

while a != 'End':


    if a.isalpha():
        if a == 'c' and not c:
            a = ""
            c = True
        if a == 'o' and not o:
            a = ""
            o = True
        if a == 'n' and not n:
            a = ""
            n = True

        if c and o and n:
            a = " "
            c = False
            o = False
            n = False
            f += b 
            b = ''

        b += a
    a = str(input())

print(f)
