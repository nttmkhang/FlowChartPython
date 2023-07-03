def Nhap():
	n = int(input('Nhap n: '))
	return n

def Tong(n):
	s = 0
	for i in range(1, n + 1, 1):
		s = s + 1/(i * (i + 1) * (i + 2))
	return s

def main():
	print('Huynh Gia Bao')
	print('Bai 043B')
	n = Nhap()
	print('S(', n,') = ', Tong(n))

if __name__ == "__main__":
	main()
