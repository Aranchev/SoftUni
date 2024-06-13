a = int(input())  #!месеци
b = 0
c = 0
d = 0
f = 0
b_s = 0
c_s = 0
d_s = 0
f_s = 0
e_s = 0


for i in range(1, a + 1):
    b = float(input())  #! за ток
    b_s += b
    c = 20  #! вода
    c_s += c
    d = 15  #! интернет
    d_s += d
    e = (b + c + d) + ((b + c + d) * 0.2)  #! др.
    e_s += e
    
f_s = (b_s + c_s + d_s + e_s) / a

print(f"Electricity: {b_s:.2f} lv")
print(f"Water: {c_s:.2f} lv")
print(f"Internet: {d_s:.2f} lv")
print(f"Other: {e_s:.2f} lv")
print(f"Average: {f_s:.2f} lv")
