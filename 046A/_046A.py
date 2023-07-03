print("Tran Thi Mong Truc Ngan")
print("Bai046A")
import math
n = int(input("Nhap n: "))
s = 0
i = 1
while i <= n:
    s = s + 1/ ((i + 1) * math.sqrt(i) + i * math.sqrt(i + 1))
    i = i + 1
print("Tong la:", s)



