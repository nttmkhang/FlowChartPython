def Nhap():
    x = float(input('Nhap x: '))
    n = int(input('Nhap n: '))
    return x, n

def TinhTong(x, n):
    s = 0
    t = 1
    m = 0
    for i in range(1, n + 1):
        t = t * x
        m = m + i
        s = s + t / m
    return s

def main():
    x, n = Nhap() 
    print('Tong la: ', TinhTong(x, n))
if __name__ == "__main__":
    print('Nguyen Hoang Anh')
    print('Bai 073B')
    main()
