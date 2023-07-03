def Nhap():
	r = float(input('Nhap ban kinh r: '))
	return r

def TheTich(r):
	return 4 * 3.14 * r * r * r / 3

def main():	
	r = Nhap()
	print('The tich hinh cau la: ', TheTich(r))

if __name__ == "__main__":
	print("Pham Nguyen Nhat Duy")
	main()
