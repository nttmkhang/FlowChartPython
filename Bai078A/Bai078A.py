print('Truong Nguyen Phuoc Tri')
print('Bai 078A')

x = float(input('Nhap x: '))
n = int(input('Nhap n: '))
s = 1
t = 1
for i in range(1, n+1):
	t = float(t * x)
	s = float(s + t)
print('S(',x,',',n,') = ', s)


