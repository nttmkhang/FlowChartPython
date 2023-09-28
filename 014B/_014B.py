def Nhap():
    x = float(input("Nhap x: "))
    return x


def TinhX32(x):
    x2 = x * x
    x4 = x2 * x2
    x8 = x4 * x4
    x16 = x8 * x8
    x32 = x16 * x16
    return x32


def main():
    x = Nhap()
    print("x^32 = ", TinhX32(x))

if __name__ == "__main__":
    print("Vo Xuan Thao")
    print("Bai 014B: ")
    main()
