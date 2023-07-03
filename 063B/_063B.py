def Nhap():
    n = int(input("Nhap n: "))
    return n
def TichCacSoLe(n):
    t = n
    tich = 1
    while t != 0:
        dv = t % 10
        if dv % 2 != 0:
            tich *= dv
        t = int(t / 10)
    return tich

def main():
    print("Cao Van Hoang")
    n = Nhap()
    kq = TichCacSoLe(n)
    print("Tich cac chu so le cua n la:",kq)

if __name__ == "__main__":
    main()
