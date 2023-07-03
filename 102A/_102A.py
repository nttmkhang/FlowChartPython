import math
print("Nguyễn Thị Tuyết Loan - 22520783 - Bài 102")
s = 0
e = 0.5
i = 2
while e >= math.pow(10,-6):
    e = 1 / i
    s = s + e
    i += 2
print("Tong", s)
