print("To Hoang Huy")
n = int(input("Nhap n: "))
s = 0
t = n
while t != 0:
    dv = t % 10
    if (dv % 2) == 0:
        s += dv
    t = int(t/10)
print("Tong cua chu so chan cua", n, "la", s)

