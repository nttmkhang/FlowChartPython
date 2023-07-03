print('Doan Quang Huy')
print('Bai 064')
def Nhap():
    n=int(input('Nhap n:'))
    return n
def ChuSoLonNhat(n):
    lc = n%10
    t=n
    while t!=0:
        dv=t%10
        if dv>lc:
            lc=dv
        t//=10
    return lc
def main():
    n=Nhap()
    kq=ChuSoLonNhat(n)
    print('Chu so lon nhat cua n la:',kq)
if __name__ == "__main__":
    main()


