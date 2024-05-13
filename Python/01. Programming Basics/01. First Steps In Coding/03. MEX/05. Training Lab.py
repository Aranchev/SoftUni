# https://judge.softuni.org/Contests/Practice/Index/1642#4
h = float(input()) * 100 # височина, в м (вх) в cm input
w = float(input()) * 100 # ширина, в м (вх) в cm input
koridor = 100
rab_m_h = 120 #дълж на раб. място
rab_m_w = 70 # шир на раб място
rab_m = rab_m_h * rab_m_w # раб място
a = h // rab_m_h  # колко места се събират в ширината
b = (w - koridor) // rab_m_w # колко места се събират в ширината
c = (a * b) - 3
print(int(c))

