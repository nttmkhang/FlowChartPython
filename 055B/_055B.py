def Nhap():
	n = int(input('Nhap n: '))
	return n

def TichUocLe(n):
	i=3
	T=1
	while(i<=n):
		if n%i==0:
			T=T*i
		i=i+2
	return T

def main():
	print("Nguyen Duy An")
	print("Bai 055B: ")
	n = Nhap()
	print("Tich uoc so le la ", TichUocLe(n))

if __name__ == "__main__":
    main()
