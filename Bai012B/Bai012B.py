def Nhap():
	print('Truong Nguyen Phuoc Tri')
	x = int(input('Nhap x: '))
	return x

def LuyThua(x):
	x2 = x * x
	x4 = x2 * x2
	x6 = x4 * x2
	return x6

def main():
	print('Bai 012B')
	x = Nhap()
	print(x,'^6 = ', LuyThua(x))

if __name__ == "__main__":
    main()


