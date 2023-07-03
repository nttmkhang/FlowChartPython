def Nhap():
	print('Truong Nguyen Phuoc Tri')
	x = float(input('Nhap x: '))
	n = int(input('Nhap n: '))
	return x, n

def Tong(x, n):
	s = 1
	t = 1
	for i in range(1, n+1):
		t = float(t * x)
		s = float(s + t)
	return s

def main():
	print('Bai 078B')
	x, n = Nhap()
	print('S(',x,',',n,') = ', Tong(x, n))

if __name__ == "__main__":
    main()