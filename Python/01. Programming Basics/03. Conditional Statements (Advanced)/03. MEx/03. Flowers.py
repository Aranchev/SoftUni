# https://judge.softuni.org/Contests/Practice/Index/1663#2
# Вход--------------------------------------------------------------------------------
a = int(input())                        # брой - хризантеми
b = int(input())                        # брой - рози
c = int(input())                        # брой - лалета
d = str(input().lower())                # сезона – [Spring, Summer, Аutumn, Winter]
e = str(input().lower())                # дали денят е празник – [Y – да / N - не]
# ------------------------------------------------------------------------------------
if d == 'spring' or d == 'summer':
    f = a * 2.00
    g = b * 4.10
    h = c * 2.50
    i = f + g + h
    if e == 'y':
        i = i + (i * 0.15)
    if d == 'spring' and c > 7:
        i = i - (i * 0.05)
    if a + b + c > 20:
        i = i - (i * 0.2)
            
    i += 2.00
elif d == 'autumn' or d == 'winter':
    f = a * 3.75
    g = b * 4.50
    h = c * 4.15
    i = f + g + h
    if e == 'y':
        i = i + (i * 0.15)
    if d == 'winter' and b >= 10:
        i -= (i * 0.1)
    if a + b + c > 20:
        i = i - (i * 0.2) 
    i += 2.00
# Изход ------------------------------------------------------------------------------
print(f'{i:.2f}')