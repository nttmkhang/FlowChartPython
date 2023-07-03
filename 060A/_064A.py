print('Doan Quang Huy')
print('Bai 064')
n=int(input('Nhap n:'))
lc = n%10
t=n
while t!=0:
    dv=t%10
    if dv>lc:
        lc=dv
    t//=10
print('Chu so lon nhat cua n la:',lc)