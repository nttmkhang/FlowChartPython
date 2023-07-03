def Nhap():
    n = int(input("Nhap n: "))
    return n
def TinhTong(n):
    s = 0
    i = 1
    while i <= n:
        s = s + i**3
        i = i + 1
    return s
def main():
    n = Nhap()
    print("S(",n,") = ",TinhTong(n))
if __name__ == "__main__":
    print('Nguyen Thanh Tai')
    print('Bai 037B')
    main()
