print("Le Toan")
print("Bai_138")
x = float(input("Nhap x: "))
if x >= 0:
	if x <= 1:
		f = 5 * x - 7
	else:
		f = 2 * (x ** 3) + 5 * (x ** 2) - 8 * x + 3
else:
	f = -2 * (x ** 3) + 6 * x + 9
print("f(", x, ") =", f)
