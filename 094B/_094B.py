import math
def Nhap():
	n = float(input('Nhap n: '))
	return n

def Tinh(n):
	s = 0
	i = 1
	while (i <= n):
		s = math.sqrt(i + s)
		i = i + 1
	return s

def main():
	n = Nhap()
	print('Tong la S(', n,') =',Tinh(n))

if __name__ == "__main__":
	print("Nguyen Huynh Phuc Lam")
	print("Bai 094B")
	main()
