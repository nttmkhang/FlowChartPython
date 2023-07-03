def Nhap():
    n = int(input('Nhap n: '))
    return n

def SoDaoNguoc(n):
    dn = 0
    t = n
    while t != 0:
        dv = int(t % 10)
        dn = dn * 10 + dv
        t = t // 10
    return dn

def main():
    n = Nhap()
    print('So dao nguoc cua ', n, ' la: ', SoDaoNguoc(n))

if __name__ == "__main__":
    print("Tran Thi Mong Truc Ngan")
    print("Bai142B")
    main()



