import math
def Nhap():
	n = int(input("Nhap n: "))
	return n

def Tong(n):
	s = 1
	for i in range(1, n + 1):
		s += 1 / (math.sqrt(i) + math.sqrt(i + 1))
	return s 

def main():
	n = Nhap()
	print("Tong la: ", Tong(n))

if __name__ == "__main__":
	print("Ho Kim Thien Nga")
	print("Bai 045B")
	main()

