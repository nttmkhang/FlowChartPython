import math
def Nhap():
    n = float(input('Nhap n: '))
    r = float(input('Nhap r: '))
    return n, r
def TinhChuVi(n, r):
    p = 2 * n * r * math.sin(3.14/n)
    return p
def main():
    n, r = Nhap()
    print ('Chu vi da giac deu noi tiep trong duong tron ban kinh',r,' la:',TinhChuVi(n, r))
if __name__ == '__main__':
    print('Nguyen Thai Binh')
    print('Bai008B')
    main()
