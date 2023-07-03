
def Nhap():
    x = int(input('Nhap x: '))
    n = int(input('Nhap n: '))
    return x, n

def Tinh(x, n):
    s = 0
    t = 1
    m = 1
    i = 1
    dau = -1
    while (i <= n):
        t = t * x
        m = m * i
        s = s + dau * t / m
        i = i + 1
        dau = -dau
    return s


def main():
    print('Bai 090b, Phù Đức Quân')
    x, n = Nhap()
    s = Tinh(x, n)
    print('Tong la: ', s)


if __name__ == "__main__":
    main()