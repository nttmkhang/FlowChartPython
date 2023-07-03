def Nhap():
	n = int(input('Nhap n: '))
	return n

def DemUocChan(n):
	dem = 0
	i = 2
	while(i<=n):
		if(n%i==0):
			dem=dem+1
		i=i+2
	return dem

def main():
	print("Nguyen Duy An")
	print("Bai 056B: ")
	n = Nhap()
	print("So luong uoc chan la : ", DemUocChan(n))

if __name__ == "__main__":
    main()
