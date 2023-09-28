print('Huynh Gia Bao')
print('Bai 139A')

a = float(input('Nhap a: '))
b = float(input('Nhap b: '))
print('Phuong trinh da nhap: ', a,'x +',b, '= 0')

if (a == 0):
    if (b == 0):
        print('Phuong trinh vo so nghiem')
    else:
        print('Phuong trinh vo nghiem')
else:   
    x = -b/a
    print('Nghiem x =',x)
