def Nhap():
    x = float(input("Nhap x: "))
    return x

def Tinhx7(x):
    x2 = x * x
    x4 = x2 * x2
    x8 = x4 * x4
    x7 = x8 / x
    return x7

def main():
    x = Nhap()
    print(x, "^7 =", Tinhx7(x))

if __name__ == "__main__":
    print("Trần Minh Chính")
    print("Bài 013: ")
    main()