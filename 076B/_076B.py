def Nhap():
	x = float(input("Nhap x: "))
	n = int(input("Nhap n: "))
	return x, n

def TinhTong(x, n):
	S = 1 + x
	t = x
	m = 1
	i = 3
	while i <= 2*n+1:
		t = t * x * x
		m = m *i * (i-1)
		S = S + t/m
		i += 2
	return S

def main():
	print('Ho Thi Thanh Thao 076B')
	x, n = Nhap()
	print("Gia tri cua S({}, {}) la: {}".format(x, n, TinhTong(x, n)))

if __name__ == "__main__":
    main()
