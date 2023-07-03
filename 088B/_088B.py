def Nhap():
	n = int(input('Nhap n: '))
	return n

def Tong(n):
	s = 0
	m = 0
	i = 1
	dau = 1
	while i <= n:
		m = m + 1
		s = s + float(dau/m)
		i = i + 1
		dau = - dau
	return s

def main():
	print('Le Quang Nhan')
	n = Nhap()
	print('Tong = ', Tong(n))

if __name__ == "__main__":
    main()