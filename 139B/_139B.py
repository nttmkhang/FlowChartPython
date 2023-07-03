def Nhap():
    a = float(input('Nhap a: '))
    b = float(input('Nhap b: '))
    return a, b

def GiaiPhuongTrinh(a, b):
    if (a == 0):
        if (b == 0):
            print('Phuong trinh vo so nghiem')
        else:
            print('Phuong trinh vo nghiem')
    else:   
        x = -b/a
        print('Nghiem x =',x)

def main():
    print('Huynh Gia Bao')
    print('Bai 139B')

    a, b = Nhap() 
    print('Phuong trinh da nhap: ', a,'x +',b, '= 0')
    GiaiPhuongTrinh(a, b)

if __name__ == "__main__":
    main()
