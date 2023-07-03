import math

print("Le Thi Bich Loan: ")
print("Bài 097A: ")

x = int (input("Nhap so x: "))
n = int (input("Nhap so n: "))
s = 0
i = 1
t = 1
while i <= n:
    t = t * x
    s = math.sqrt(t + s)
    i = i + 1
print("S = ", s)
