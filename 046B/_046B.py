import math
def Nhap():
	n = int(input("Nhap n: "))
	return n

def Tong(n):
	s = 0
	for i in range(1, n + 1):
		s = s + 1 / ((i + 1) * math.sqrt(i) + i * math.sqrt(i + 1))
	return s

def main():
	n = Nhap()
	print("Tong la: ", Tong(n))

if __name__ == "__main__":
	print("Tran Thi Mong Truc Ngan")
	print("Bai046B")
	main()


