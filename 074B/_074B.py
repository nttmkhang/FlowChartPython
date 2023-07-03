def Nhap():
    x = float(input('Nhap x: '))
    n = int(input('Nhap n: '))
    return x, n
def Tong(x, n):
    s = 0
    t = 1
    m = 1
    i = 1
    while i <= n:
        t = t * x
        m = m * i
        s = s + t / m
        i = i + 1
    return s
def main():
    x, n = Nhap()
    print("S(", x, ",", n, ") la: ", Tong(x, n))
if __name__ == '__main__':
    print('Nguyen Thai Binh')
    print('Bai074B')
    main()
