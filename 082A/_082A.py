import math

print("Le Thi Bich Hang")
print("Bai 082A")

x = float(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 0
t = 1
for i in range(1, n+1):
    t = t * math.sin(x)
    s = s + t
print("Tong la: ", s)
