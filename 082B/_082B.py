import math

def Nhap():
    x = float(input("Nhap x: "))
    n = int(input("Nhap n: "))
    return x, n

def TinhTong(x, n):
    s = 0
    t = 1
    for i in range(1, n+1):
        t = t * math.sin(x)
        s = s + t
    return s

def main():
    print("Le Thi Bich Hang")
    print("Bai 082B")
    x, n = Nhap()
    print("Tong la: ", TinhTong(x, n))

if __name__ == "__main__":
    main()

