def nhap():
    n = int (input("Nhap so n: "))
    return n
    
def xuat(s):
    print("Tong la: ", s)
    
def tinhTong(n):
    s = 0
    i = 2
    while i <= n:
        s = (i + s) ** (1 / i)
        i = i + 1
    return s

def main():
    print('Phan Trọng Tính')
    print('Bai 098B')
    n = nhap()
    s = tinhTong(n)
    xuat(s)

if __name__ == "__main__":
    main()
