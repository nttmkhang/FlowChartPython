print('Tran Ngoc Nhat Vy')
print('Bai 081B')

def Nhap():
	x = float(input('Nhap x: '))
	n = int(input('Nhap n: '))
	return x, n

def Tong(x, n):
	s = 0
	m = 1
	for i in range(0, n + 1):
		m = m * (x + i)
		s = s + float(1 / m)
		i = i + 1
	return s

def main():
	x, n = Nhap()
	print('S(',x,',',n,") = ", Tong(x, n))

if __name__ == "__main__":
    main()


