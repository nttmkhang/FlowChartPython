import math

def Nhap():
    x = float(input('Nhap x: '))
    y = float(input('Nhap y: '))
    return x, y

def TinhChuVi(x1,y1,x2,y2,x3,y3):
    a = math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))
    b = math.sqrt((x3 - x2)*(x3 - x2) + (y3 - y2)*(y3 - y2))
    c = math.sqrt((x3 - x1)*(x3 - x1) + (y3 - y1)*(y3 - y1))
    p = a + b + c
    return p

def main(): 
    print('Ho Thi Thanh Thao 010B')
    print('Nhap toa do diem thu nhat:')
    x1, y1 = Nhap()
    print('Nhap toa do diem thu hai:')
    x2, y2 = Nhap()
    print('Nhap toa do diem thu ba:')
    x3, y3 = Nhap()
    print('Chu vi tam giac la: ', TinhChuVi(x1,y1,x2,y2,x3,y3))

if __name__ == "__main__":
    main()