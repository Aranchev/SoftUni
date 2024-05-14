# https://judge.softuni.org/Contests/Practice/Index/1663#1
# Вход ----------------------------------------------------------------------------------
a = float(input())          # броят младши велосипедисти
b = float(input())          # броят старши велосипедисти
c = str(input().lower())    # вид трасе – "trail", "cross-country", "downhill" или "road"
#----------------------------------------------------------------------------------------
if c == 'trail':
    j = 5.50 * a
    s = 7 * b
    d = j + s
    d = d - (d * 0.05)
elif c == 'cross-country':
    j = 8 * a
    s = 9.50 * b
    d = j + s
    if a + b >= 50:
        d = d - (d * 0.25)
    d = d - (d * 0.05)      # това извади 5 процента от онази сума, от която са извадени 25 процента.
elif c == 'downhill':
    j = 12.25 * a
    s = 13.75 * b
    d = j + s
    d = d - (d * 0.05)
elif c == 'road':
    j = 20 * a
    s = 21.50 * b
    d = j + s
    d = d - (d * 0.05)
# Изход ---------------------------------------------------------------------------------
print(f'{d:.2f}')
