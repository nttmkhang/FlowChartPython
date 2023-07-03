def Nhap():
	x = int(input("Nhap x: "))
	y = int(input("Nhap y: "))
	return x, y

def XuatNamNhuan(x, y):
	n = x
	while n <= y:
		dk1 = (n % 4 == 0) and (n % 100 != 0)
		dk2 = n % 400
		if dk1 and dk2:
			print(n, end = ' ')
		n += 1

def main():
	x, y = Nhap()
	print("Nam nhuan trong doan [", x, ",", y, "]: ")	
	XuatNamNhuan(x, y)

if __name__ == "__main__":
	print("Le Toan")
	print("Bai_136")
	main()
