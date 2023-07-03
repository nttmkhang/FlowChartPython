print('Doan Quang Huy')
print('Bai 160')
n=int(input('Nhap n:'))
dt=n
while dt>=10:
    dt = dt // 10
t = n
dem = 0
while t!=0:
    dv = t  %10
    if ( dv == dt ):
        dem+=1
    t = t // 10
print('So chu so dau tien cua n la:',dem)