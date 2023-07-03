print('Nguyen Vu Binh')
print('Bai_149B')
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

def main():
    print('Nhap so a: ')
    a = Nhap()
    print('Nhap so b: ')
    b = Nhap()
    ucln = UCLN(a, b)
    print('UCLN(',a, ',', b, '):', ucln)

if __name__ == "__main__":
    main()