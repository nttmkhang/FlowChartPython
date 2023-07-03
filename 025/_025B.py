def Nhap():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    return a, b

def HoanVi(a,b):
    temp = a
    a = b
    b = temp
    return a, b

def Xuat(a, b):
    print("Sau khi hoan vi: a = ", a, "b = ",b)

def main():
    print("Bui Thi Hoang Giang")
    print("Bai 025B")
    a, b = Nhap()
    print("Ban dau: a = ", a, "b = ",b)
    a, b = HoanVi(a,b)
    Xuat(a,b)

if __name__ == "__main__":
    main()
