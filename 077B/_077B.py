def Nhap():
	k = float(input("Nhap k: "))
	n = int(input("Nhap n: "))
	return k, n

def TinhTong(k, n):
	s = 0
	i = 1
	while( i <= n):
		s = s + pow(i, k)
		i = i + 1
	return s

def main():
	print("Mai Dinh Khoi")
	print('Bai 077B')
	k, n = Nhap()
	print("Tong la: ", TinhTong(k, n))
	

if __name__ == "__main__":
    main()


