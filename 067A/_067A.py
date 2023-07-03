print("Trần Trọng Khiêm")
print("Bài 067")

n = int(input("Nhap n:"))
lc = n % 10
t = n
while(t != 0):
	dv = (t%10)
	if(dv < lc):
		lc = dv
	t = int(t/10)

print('Chu so nho nhat trong n la: ', lc)

