print("Le Toan")
print("Bai_136")
x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
print("Nam nhuan trong doan [", x, ",", y, "]: ")
n = x
while n <= y:
	dk1 = (n % 4 == 0) and (n % 100 != 0)
	dk2 = n % 400
	if dk1 and dk2:
		print(n, end = ' ')
	n += 1
