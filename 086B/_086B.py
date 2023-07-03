def Nhap():
	x = float(input('Nhap x: '))
	n = float(input('Nhap n: '))
	return x, n

def Tinh(x, n):
	s = 0
	t = 1
	dau = -1
	i = 2
	while(i <= 2 * n):
		t = float(t * x * x)
		s = float(s + dau * t)
		i = i + 2
		dau = -dau
	return s

def main():
	print('Pham Tran Anh Khoi')
	print('Bai 86B')
	x, n = Nhap()
	print('Tong S la: ', Tinh(x, n))

if __name__ == "__main__":
    main()
