print('Doan Quang Huy')
print('Bai 160')
def Nhap():
    n=int(input('Nhap n:'))
    return n
def DemChuSoDauTien(n):
    dt=n
    while dt>=10:
        dt = dt // 10
    t = n
    dem = 0
    while t!=0:
        dv = t  %10
        if ( dv == dt ):
            dem+=1
        t = t // 10
    return dem
def main():
    n=Nhap()
    kq=DemChuSoDauTien(n)
    print('So chu so dau tien cua n la:',kq)
if __name__ == "__main__":
    main()
