def Nhap():
    n=int(input("Nhap n: "))
    return n
def TichChuSo(n):
    tich=1
    t=n
    while (t!=0):
        dv=t%10
        tich=tich*dv
        t=int(t/10)
    return tich
def main():
    print("Nguyen Tan Duy")
    print("Bai 060B")
    n = Nhap()
    print('Tich cac chu so la: ', TichChuSo(n))

if __name__ == "__main__":
    main()