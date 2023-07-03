def Nhap():
    x = int(input("Nhap x: "))

def HamLuyThua(x):
    x2 = x * x
    x4 = x2 * x2
    x5 = x4 * x
    x8 = x4 * x4
    x13 = x5 * x8
    return x13

def main():
    print('Bui Thi Nhu Y')
    print('Bai 019B')
    x = Nhap()
    print('Luy thua 13 cua ', x, ' la: ', HamLuyThua(x))


if __name__ == "__main__":
    main()