from math import sin


x = int(input("Nhap x:"))
n = int(input("Nhap n:"))
s = 0
t = 1
i = 1
while i <= n:
    t *= x
    s += sin(t)
    i += 1
print("Bai 83A: Tran Dong Dong")
print("S=", s)
