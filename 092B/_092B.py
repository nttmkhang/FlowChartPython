def Nhap():
    x = float(input("Nhap x: "))
    n = int(input("Nhap n: "))
    return x, n
def Tong(x, n):
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
    return s
def main():
    x, n = Nhap()
    print("S(", x, ",", n, ") = ", Tong(x, n))
if __name__ == "__main__":
    print("Nguyen Cao Quoc Bao")
    print("Bai 092B")
    main()