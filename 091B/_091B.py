def Nhap():
    print("Nguyen Huynh Phuc Thinh")
    x = float(input("Nhap x: "))
    n = float(input("Nhap n: "))
    return x,n

def Tinh(x,n):
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
    return s

def main():
    print("Bai 091B: ")
    x , n = Nhap()
    print("S(", x, ",", n, ")= ", Tinh(x,n))

if __name__ == "__main__":
    main()