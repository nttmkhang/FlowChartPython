print('Nguyen Quoc Thang')
def Tinh(n):
	s = 0
	i = 1
	while i <= n:
		s = s + i * (i + 1) * (i + 2)
		i = i + 1
	return s
def Nhap():
	x = int(input('Nhap n: '))
	return x
def main():
	n = Nhap()
	print('S(n) = ', Tinh(n))
if __name__ == "__main__":
    main()