# https://judge.softuni.org/Contests/Compete/Index/2416#7
e = int(input()) # час на изпита
b = int(input()) # минута на изпита
c = int(input()) # час на пристигане
d = int(input()) # минута на пристигане

f = (e * 60) + b # време на изпита в минути
g = (c * 60) + d # време на пристигане в минути

j = f // 60      # час на изпита
h = f % 60       # минути на изпита

if f - g < 0:   # (f) време на изпита в минути - (g) време на пристигане в минути
    e = 'Late'
elif f - g <= 30 or f == g:
    e = 'On time' 
elif f - g >= 30:
    e = 'Early'

print(e)

if f > g and f - g < 60: # f > g - подранил е
    print(f'{f-g} minutes before the start')
if f > g and f - g >= 60:
    print(f'{(f-g) // 60}:{(f-g) % 60:02d} hours before the start')
elif g > f and g - f < 60:
    print(f'{g-f} minutes after the start')
elif g > f and g - f >= 60:
    print(f'{(g-f) // 60}:{(g-f) % 60:02d} hours after the start')