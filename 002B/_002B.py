def Nhap():
	r = float(input('Ban kinh: '))
	return r

def DienTich(r):
	return 3.14 * r * r

def main():
	print("Bài 002")
	r = Nhap()
	print('Dien tich duong tron la: ', DienTich(r))

if __name__ == "__main__":
	print("Trần Trọng Khiêm")
	main()