print("Tang Thanh Thien")
n = int(input("Nhap n: "))
att = 1
at = 1
i = 2
while i <= n:
    ahh = at + att
    i += 1
    att = at
    at = ahh
print("So hang thu", n,"cua day la: ", ahh)

