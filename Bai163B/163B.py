
def Nhap():
	n = int(input('Nhap n: '))
	return n

def UocLeLonNhat(n):
	t=n 
	while(t%2==0):
		t=t/2 
	return t

def main():
	print('Phan Trọng Tính')
	print("Bai 163B")
	n = Nhap()
	print("Uoc le lon nhat la ", UocLeLonNhat(n))

if __name__ == "__main__":
    main()
