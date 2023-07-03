def Nhap():
    n = int(input("nhap n:"))
    return n
def Tinh(n):
    a1=2
    for i in range(2,n+1,1):
        at = 5 * a1 + 2 * 3 ** i - 6 * 7 ** 9 +12
        ahh = 5 * at + 2 * 3 ** i - 6 * 7 ** 9 +12
        at = ahh
    return at
def main():
    n=Nhap()
    at=Tinh(n)
    print("Phan Nguyen Khoa - Bai 114B")
    print("So hang thu n cua day la: ",at)
if __name__ == "__main__":
    main()