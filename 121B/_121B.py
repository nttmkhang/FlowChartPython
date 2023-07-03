def Nhap():
    n = int(input("Nhap n: "))
    return n

def TinhSoHangThun(n):
    att = 1
    at = 1
    ahh = 0
    for i in range (2, n + 1):
        ahh = at + att
        att = at
        at = ahh
    return ahh

def main():
    print("Tang Thanh Thien")
    n = Nhap()
    print("So hang thu ", n,"cua day la: ", TinhSoHangThun(n))

if __name__ == "__main__":
    main()


