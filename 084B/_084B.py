import math
def Nhap():
    x = float(input("Nhap x: "))
    n = int(input("nhap n: "))
    return x,n

def Tong(x, n):
    s = 0
    t = x
    i = 1
    while i < n:
        t = math.sin(t)
        s += t
        i += 1
    return s

def main():
    print("Nguyen Cong Tai")    
    print("Bai 084A")
    x,n = Nhap()
    print("s = ", Tong(x,n))

if __name__ == "__main__":
    main()

