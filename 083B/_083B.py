from cmath import sin


def Nhap():
    x = int(input("Nhap x:"))
    n = int(input("Nhap n:"))
    return x, n

def TinhTong(x, n):
    s = 0
    t = 1
    i = 1
    while i <= n:
        t *= x
        s += sin(t)
        i += 1
    return s

def main():
    x, n = Nhap()
    print("Bai 83B: Tran Dong Dong")
    print("s =", TinhTong(x,n))

if __name__ == "__main__":
    main()
