def Nhap():
    x = int(input("Nhap x:"))
    return x

def Tinhx11(x):
    x2 = x * x
    x4 = x2 * x2
    x8 = x4 * x4
    x10 = x8 * x2
    x11 = x10 * x
    return x11

def main():
    x = Nhap()
    x11 = Tinhx11(x)
    print("Bai 17B: Tran Dong Dong")
    print(x, "^ 11 =", x11)

if __name__ == "__main__":
    main()
