def Nhap():
    n = int(input("Nhap n: "))
    return n
def TinhTong(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i*(i + 1)
    return s
def main():
    n = Nhap();
    print("S(",n,") = ", TinhTong(n))
if __name__ == '__main__':
    print('Nguyen Thanh Tai')
    print('Bai 039B')
    main()

