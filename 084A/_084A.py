print("Nguyen Cong Tai")    
print("Bai 084A")

import math
x = float(input("Nhap x: "))
n = int(input("nhap n: "))

s = 0
t = x
i = 1

while i < n:
    t = math.sin(t)
    s += t
    i += 1
print("s= ", s) 

