print("Nguyen Cao Quoc Bao")
print("Bai 092A")
x = float(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 1 - x
t = x
m = 1
i = 3
dau = +1
for i in range(3, 2 * n + 3, 2):
    t = t * x * x
    m = m * i * (i - 1)
    s = s + dau * t / m
    dau = -dau
print("S(", x, ",", n, ") = ", s)
