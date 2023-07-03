def Nhap():
	x = float(input('Nhap x: '))
	n = int(input('Nhap n: '))
	return x,n 

def S(x, n):
	s = x
	t = x
	i = 3
	for i in range(i, 2 * n + 2):
		t = t * x * x
		s = s + t
		i = i + 2
	return s

def main():
	x, n = Nhap()
	print('S(x,n) = ' , S(x,n))

if __name__ == "__main__":
	print("Nguyễn Phước Hưng")
	print('Bai 071:')
	main()