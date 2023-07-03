def Nhap():
    x = float(input("Nhap x: "))
    n = float(input("Nhap n: "))
    return x, n


def TinhS(x, n):
    s = 1
    t = 1
    i = 1
    while(i<=n):
        t = t * x
        s = s + (i + 1 ) * t
        i = i + 1
    return s

def main():
    x, n = Nhap()
    print("S = ", TinhS(x, n))

if __name__ == "__main__":
    print ('Vo Xuan Thao')
    print('Bai 080B: ')
    main()

