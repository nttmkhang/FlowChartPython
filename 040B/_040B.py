print('Nguyen Quoc Thang')
def Tinh(n):
	s = 0
	for i in range(1,n+1):
		s = s + i*(i+1)
	return s
def Nhap():
	x = int(input('Nhap n: '))
	return x
def main():
	n = Nhap()
	print('S(n) = ', Tinh(n))
if __name__ == "__main__":
    main()