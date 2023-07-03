def Nhap():
	x = float(input('Nhap x: '))
	return x

def LuyThua14(x):
	x2 = x * x
	x4 = x2 * x2 
	x6 = x4 * x2 
	x8 = x4 * x4 
	x14 = x8 * x6
	return x14

def main():
	print('Pham Tran Anh Khoi')
	print('Bai 20')
	x = Nhap()
	print('x14 = ', LuyThua14(x))

if __name__ == "__main__":
    main()