import math

def nhap():
    x = int (input("Nhap so x: "))
    n = int (input("Nhap so n: "))
    return x, n
    
def xuat(s):
    print("Tong la: ", s)
    
def tinhTong():
    x, n = nhap()
    s = 0
    i = 1
    t = 1
    while i <= n:
        t = t * x
        s = math.sqrt(t + s)
        i = i + 1
    xuat(s)

def main():
    print("Bai 097B: 21521083")
    tinhTong()

if __name__ == "__main__":
    main()
