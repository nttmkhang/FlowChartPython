def Nhap():
	c = float(input('Nhap do C: '))
	return c

def DoF(c):
	return (9 / 5) * c + 32

def main():
	print('Nguyen Minh Phap')
	print('Bai 006:')
	c = Nhap()
	print('Do F: ' , DoF(c) , sep="")

if __name__ == "__main__":
    main()
