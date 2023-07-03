print('Tran Ngoc Nhat Vy')
print('Bai 015B')

def Nhap():
	x = int(input('Nhap x: '))
	return x

def LuyThua(x):
	x2 = x * x
	x4 = x2 * x2
	x8 = x4 * x4
	x16 = x8 * x8
	x32 = x16 * x16
	x64 = x32 * x32
	return x64

def main():
	x = Nhap()
	print('Luy thua 64 cua', x, 'la : ', LuyThua(x))

if __name__ == "__main__":
    main()
