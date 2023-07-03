print('Nguyen Hoang Anh')
print('Bai 073A')
x = float(input('Nhap x: '))
n = int(input('Nhap n: '))
s = 0
t = 1
m = 0
for i in range(1, n + 1):
    t = t * x
    m = m + i
    s = s + t / m
print('Tong la: ', s)
