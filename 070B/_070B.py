def Nhap():
	x = float(input("Nhap x: "))
	n = int(input('Nhap n: '))
	return x,n

def Tong(x,n):
	s = 0
	t = 1
	i = 2
	while(i<=2*n):
		t = t * x * x
		s = s + t
		i = i + 2
	return s

def main():	
	x,n = Nhap()
	print('Tong la:', Tong(x,n))

if __name__ == "__main__":
	print("Pham Nguyen Nhat Duy")
	main()
