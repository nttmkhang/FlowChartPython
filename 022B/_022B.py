def Nhap():
	n = int(input('Nhap n: '))
	return n

def TimDonVi(n):
	dv = n % 10
	return dv

def main():
	print('Le Quang Nhan')
	print('Bai 022B')
	n = Nhap()
	print('Chu so don vi: ', TimDonVi(n))

if __name__ == "__main__":
    main()