
def Nhap():
	n = int(input('Nhập một số nguyên dương n: '))
	return n

def ChuSoHangTram(n):
	ht = int(n/100%10)
	return ht

def main():
	print("Bai 24b, Phù Đức Quân")
	n = Nhap()
	print("Chữ số hàng trăm của", n, "là:", ChuSoHangTram(n))
if __name__ == "__main__":
    main()
