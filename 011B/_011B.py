from math import sqrt


def Nhap():
	x = float(input('Nhap x: '))
	y = float(input('Nhap y: '))
	return x, y

def TinhDienTichTamGiac(x1, y1, x2, y2, x3, y3):
	a = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
	b = sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2))
	c = sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))

	p = (a + b + c) / 2
	s = sqrt(p * (p - a) * (p - b) * (p - c))

	return s

def main():
	print("Mai Dinh Khoi")
	print('Bai 011B')
	print("Nhap toa do diem thu nhat")
	x1, y1 = Nhap()
	print("Nhap toa do diem thu hai")
	x2, y2 = Nhap()
	print("Nhap toa do diem thu ba")
	x3, y3 = Nhap()
	print("Dien tich tam giac la: ", TinhDienTichTamGiac(x1, y1, x2, y2, x3, y3))
	

if __name__ == "__main__":
    main()

