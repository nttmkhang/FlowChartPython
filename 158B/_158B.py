def Nhap():
	n = int(input("Nhap n: "))
	return n

def DemLonNhat(n):
	lc = n % 10
	dem = 0
	t = n
	while (t != 0):
		dv = t % 10
		if(dv > lc):
			lc = dv
		t = int(t / 10)
	t = n
	while (t != 0):
		dv = t % 10
		if( dv == lc):
			 dem = dem + 1
		t = int(t / 10)
	return dem

def main():
	print ("To Hoang Huy")
	n = Nhap()
	print("So chu so lon nhat cua n la: ", DemLonNhat(n))

if __name__ == "__main__":
    main()
