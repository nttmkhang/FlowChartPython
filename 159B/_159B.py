def Nhap():
    n = int(input("Nhap n: "))
    return n

def demChuSoNhoNhat(n):
    lc = n % 10
    dem = 0
    t = n
    while t != 0:
        dv = t % 10
        if dv < lc:
            lc = dv
        t //= 10
    t = n
    while t != 0:
        dv = t % 10
        if dv == lc:
            dem+=1
        t //= 10
    return dem

def main():
    print("Cao Van Hoang")
    n = Nhap()
    kq = demChuSoNhoNhat(n)
    print("So chu so nho nhat cua n la: ",kq)

if __name__ == "__main__":
    main()