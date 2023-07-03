import math
from re import M 
def Nhap():
	x = int(input('Nhap x: '))
	n = int(input('Nhap n: '))
	return x,n
def Tinh(x,n):
	s = 1
	t = 1
	m = 1
	i = 2
	while i <= 2 * n:
		t = t * x * x
		m = m * i * (i - 1)
		s = s + t/m
		i = i + 2
	return s
def main():
	x,n = Nhap()
	print("S(" , x, ",", n, ") = ", Tinh(x,n))
if __name__ == "__main__":
	print("Le Thi Thu Hien")
	print('Bai 075B')
	main()
