def Nhap():
	print("Nguyen Huynh Phuc Lam")
	n = int(input('Nhap n: '))
	return n

def Tong(n):
	s = 0
	for i in range(2, 2 * n + 1, 2):
		s = s + 1 / i
	return s

def main():
	print("Bai 030B");
	n = Nhap()
	print('Tong la S(', n, ') =', Tong(n))

if __name__ == "__main__":
    main()
