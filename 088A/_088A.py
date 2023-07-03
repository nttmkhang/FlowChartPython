print('Le Quang Nhan')

n = int(input('Nhap n: '))
s = 0
m = 0
i = 1
dau = 1

while i <= n:
    m = m + 1
    s = s + float(dau/m)
    i = i + 1
    dau = - dau

print('Tong = ', s)

