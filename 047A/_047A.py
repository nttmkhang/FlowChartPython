import math as m
print("Tran Tue Tanh")
print("Bai 047A")
n = int(input("Nhap n: "))
s = 0
for i in range(1, n + 1):
    s = s + m.sqrt(1 + 1 / i ** 2 + 1 / (i + 1) ** 2)
print("S(n): ", s)
