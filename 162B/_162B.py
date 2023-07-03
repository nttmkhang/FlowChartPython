def Nhap():
    n = int(input("Nhap n: "))
    return n
def KiemTra(n):
    flag = 1
    t = n
    while t >= 10:
        dv = t % 10
        hc = (t/10) % 10
        if hc < dv:
            flag = 0
        t = t / 10
    return flag
def main():
    n = Nhap()
    flag = KiemTra(n)
    print("Nguyễn Thị Tuyết Loan - 22520783 - Bài 162")
    if flag == 1:
        print("Giam")
    else:
        print("Khong giam")
if __name__ == "__main__":
    main()