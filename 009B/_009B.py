import math 
def Nhap():
	n = float(input('Nhap n: '))
	r = float(input('Nhap r: '))
	return n,r
def Tinh(n,r):
	return (0.5* n * r * r * math.sin(3.14 * 2/n))
def main():
	n,r = Nhap()
	print('Dien tich da giac ',n,' canh noi tiep duong tron ban kinh ',r,' la: ', Tinh(n,r))
if __name__ == "__main__":
	print('Bai 009B')
	print("Le Thi Thu Hien")
	main()
