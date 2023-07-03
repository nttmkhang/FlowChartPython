import math 
def Nhap():
	n = int(input("Nhap vao so nguyen duong n: "))
	return n

def ChuSoDauTien(n):
	while ( n > 0 ):
		k = n % 10
		n = n // 10
	return k

def main():
	n = Nhap()
	x = ChuSoDauTien(n)
	print("Chu so dau tien cua n la", x)

if __name__ == "__main__":
	print ("Bai 141B")
	print ("Ho Kim Thien Nga")
	main()
    
