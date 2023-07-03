print("Bai 030A")
print("Nguyen Huynh Phuc Lam ")

n = int(input("Nhap n: "))
s = 0
for i in range(2, 2 * n + 1, 2):
    s = s + 1 / i
print("S(", n, ") =", s)
