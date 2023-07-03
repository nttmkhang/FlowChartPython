def Nhap():
	n = int(input('Nhap n: '))
	return n

def ChuSoNhoNhat(n):
	lc = n % 10
	t = n
	while(t != 0):
		dv = (t%10)
		if(dv < lc):
			lc = dv
		t = int(t/10)
	return lc

def main():
	print("Bài 067")
	n = Nhap()
	print('Chu so nho nhat trong n la: ', ChuSoNhoNhat(n))

if __name__ == "__main__":
	print("Trần Trọng Khiêm")
	main()