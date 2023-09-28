print("Nguyen Huynh Phuc Thinh")
print("Bai 091A: ")
x = float(input("Nhap x: "))
n = float(input("Nhap n: "))
s = -1
t = 1
m = 1
i = 2
dau = 1
while(i <= 2 * n):
    t = t * x * x
    m = m * i * (i - 1)
    s = s + dau * (t / m)
    i = i + 2
    dau = -1 * dau
print("S(", x, ",", n, ")= ", s)