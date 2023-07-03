def Nhap():
    f = float(input('Nhap do F: '))
    return f
def TinhDoC(f):
    c = 5 * (f - 32) / 9
    return c
def main():
    f = Nhap()
    print('Do C: ', TinhDoC(f))
if __name__ == "__main__":
    print('Nguyen Hoang Anh')
    print('Bai 007B')
    main()
