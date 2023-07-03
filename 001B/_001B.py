import math
def Nhap():
	x = float(input('Nhap x: '))
	y = float(input('Nhap y: '))
	return x, y
def KhoangCach(x1, y1, x2, y2):
	return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
def main():
	print('Bai 001B:')
	print('Nhap toa do diem thu nhat: ')
	x1, y1 = Nhap()
	print('Nhap toa do diem thu hai: ')
	x2, y2 = Nhap()
	print('Khoang cach giua hai diem la: ', KhoangCach(x1, y1, x2, y2))
if __name__ == "__main__":
	print('Nguyen Minh Phap')
	main()
