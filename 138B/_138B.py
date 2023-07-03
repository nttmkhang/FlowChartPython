def Nhap():
	x = int(input("Nhap x: "))
	return x

def f(x):
	if x >= 0:
		if x <= 1:
			f = 5 * x - 7
		else:
			f = 2 * (x ** 3) + 5 * (x ** 2) - 8 * x + 3
	else:
		f = -2 * (x ** 3) + 6 * x + 9
	return f

def main():
	x = Nhap()
	print("f(", x, ") =", f(x))

if __name__ == "__main__":
	print("Le Toan")
	print("Bai_138")
	main()
