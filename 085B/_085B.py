def Nhap():
	x = int(input('Nhap x: '))
	n = int(input('Nhap n: '))
	return x, n

def Tinh(x, n):
	s = 0
	t = 1
	i = 1
	dau = +1
	while ( i <= n):
		t = t * x
		s = s+ dau * t
		i = i + 1
		dau = -dau 
	return s

def main():
	print('Bui Thi Nhu Y')
	print ('Bai 85')
	x, n = Nhap()
	print('S = ', Tinh(x, n))

if __name__ == "__main__":
    main()
