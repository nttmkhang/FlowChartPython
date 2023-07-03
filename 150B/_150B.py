print('Nguyen Vu Binh')
print('Bai 150B')

def Nhap():
    n = int(input())
    return n

def UCLN(a, b):
    m = abs(a)
    n = abs(b)
    while m * n != 0:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m + n

def BCNN(a, b, ucln):
    return abs(a * b) / ucln

def Xuat(a, b, bcnn):
    print('BCNN(',a, ',', b, '):', bcnn)

def main():
    print('Nhap so a: ')
    a = Nhap()
    print('Nhap so b: ')
    b = Nhap()
    ucln = UCLN(a, b)
    bcnn = BCNN(a, b, ucln)
    Xuat(a, b, bcnn)

if __name__ == "__main__":
    main()
