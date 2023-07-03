
def Nhap():
    n = int(input("Nhap n: "))
    return n


def Tong(n):
    s = 0
    m = 0
    i = 1
    while i <= n:
        m = m + i
        s = s + 1 / m
        i = i + 1
    return s


def main():
    n = Nhap()
    print("Tong: ", Tong(n))

if __name__ == "__main__":
    print('Nguyen Phuoc Hung')
    print('Bai 072')
    main()