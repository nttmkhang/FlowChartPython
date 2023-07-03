
def Nhap():
	n = int(input('Nhap n: '))
	return n

def Tong(n):
	s = 0
	t = 1
	for i in range(1, n + 1):
		t *= i
		s += t
	return s

def main():
	n = Nhap()
	print('Tong la: ', Tong(n))

if __name__ == "__main__":
	print('Nguyen Trong Ninh')
	print('Bai 068')
	main()