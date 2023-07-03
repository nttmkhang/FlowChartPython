print("Nguyen Huynh Phuc Lam")
print("Bai 094A")
import math
n = float(input("Nhap n: "))
s = 0
i = 1
while (i <= n):
    s = math.sqrt(i + s)
    i = i + 1
print("S(", n, ") =", s)
