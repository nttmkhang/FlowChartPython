def Nhap():
	x = float(input("Nhap x: "))
	y = float(input("Nhap y: "))
	z = float(input("Nhap z: "))
	return x, y, z

def KiemTraDangThuc(x, y, z):
	if x <= y and y <= z:
		return 1
	else:
		return 0

def main():
	x, y, z = Nhap()
	print(x, "<=", y, "and", y, "<=", z)
	if KiemTraDangThuc(x, y, z) == 1:
		print("BDT dung")
	else:
		print("BDT sai")
		

if __name__ == "__main__":
	print("Le Toan")
	print("Bai_134")
	main()