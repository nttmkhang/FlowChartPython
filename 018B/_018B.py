def Nhap():
	x = float(input("Nhap x: "))
	return x

def Xmu12(x):
	x2 = x * x
	x4 = x2 * x2
	x8 = x4 * x4
	x12 = x8 * x4
	return x12

def main():
	print("Nguyen Cong Tai")
	print("Bai 018B")
	x = Nhap()
	print("x^12 = ", Xmu12(x))

if __name__ == "__main__":
    main()
