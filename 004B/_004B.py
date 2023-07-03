import math

def Nhap():
    r = float(input("Nhap r: "))
    return r

def DienTichXungQuanh(r):
	result = 4 * math.pi * pow(r, 2)
	return result

def main():
	r = Nhap()
	print("Dien tich xung quanh hinh cau: ", DienTichXungQuanh(r))

if __name__ == "__main__":
	print("Tran Tuan Vu")
    main()
