print("Pham Hoang Duy")
print("Bai 161")
def Nhap():
    n = int(input("Nhap n: "))
    return n
def KiemTra(n):
    flag = 1
    t = n
    while t>=10:
        dv = t % 10
        hc = (int(t / 10) % 10)
        if hc > dv:
            flag = 0
        t //= 10
    if flag == 1:
        return 1
    return 0
def Xuat(n):
    if KiemTra(n) == 1:
        print(n,"co cac chu so tang dan tu trai sang phai!")
    else:
        print(n,"co cac chu so khong tang dan tu trai sang phai!")
def main():
    n = Nhap()
    Xuat(n)
if __name__ == "__main__":
    main()

