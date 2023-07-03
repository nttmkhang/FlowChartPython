def Nhap():
    x = float(input("Nhap x: "))
    return x

def Tinhx9(x):
    x2 = x * x
    x4 = x2 * x2
    x8 = x4 * x4
    x9 = x * x8
    return x9

def main():
    print("Le Thi Bich Hang")
    print("Bai 016B")
    x = Nhap()
    print("x^9 = ", Tinhx9(x))

if __name__ == "__main__":
    main()
