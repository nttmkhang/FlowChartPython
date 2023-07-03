import math

def Nhap():
    n = int(input("Nhap n: "))
    return n

def Xuli(n):
    s = 0
    t = 1
    for i in range(1, n + 1, 1):
        t = t * i
        s = math.pow(s + t, 1/(i + 1))
    return s

def main():
    n = Nhap()
    S = Xuli(n)
    print("Bai 100B")
    print("S(", n, ") = ", S)

if __name__ == "__main__":
    print("Ho Minh Tri")
    main()

