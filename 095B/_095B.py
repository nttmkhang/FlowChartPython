import math
def Nhap():
    n = int(input("Nhap n: "))
    return n
def Tong(n):
    s = 0
    i = n
    for i in reversed(range(1, n + 1)):
        s = math.sqrt(i + s)
    return s
def main():
    n = Nhap()
    print("S(", n,") = ", Tong(n))
if __name__ == "__main__":
    print("Nguyen Cao Quoc Bao")
    print("Bai 095B")
    main()
