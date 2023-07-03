def Nhap():
	a = float(input('Nhap a: '))
	b = float(input('Nhap b: '))
	return a,b

def XuLy (a,b):
	if(a<0):
		a=-a
	if(b<0):
		b=-b;
	return a,b
	
def main():
	print("Nguyen Duy An")
	print("Bai 125B : ")
	a,b = Nhap()
	a1,b1 =XuLy(a,b)
	print("a : ",a1)
	print("b : ",b1)

if __name__ == "__main__":
    main()