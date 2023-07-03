print('Pham Tran Anh Khoi')
print('Bai 86A')
x = float(input('Nhap x: '))
n = float(input('Nhap n: '))
s = 0
t = 1
dau = -1
i = 2
while(i <= 2 * n):
	t = float(t * x * x)
	s = float(s + dau * t)
	i = i + 2
	dau = -dau
print('Tong S la: ', s)