import math
print("Nguyen Cao Quoc Bao")
print("Bai 095A")
n = int(input("Nhap n: "))
s = 0
i = n
for i in reversed(range(1, n + 1)):
    s = math.sqrt(i + s)
print("S(", n,") = ", s)
