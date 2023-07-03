def Nhap():
    x = int(input("Nhap x:"))
    return x
def TinhF(x):
    if (x >= 5):
        f = 2 * x * x + 5 * x + 9
    else:
        f = -2 * x * x + 4 * x - 9
    return f
def main():
    print("Nguyen Xuan Quang")
    print("Bai 137B")
    x = Nhap()
    f = TinhF(x)
    print("f = ", f)
if __name__ == "__main__":
    main()


