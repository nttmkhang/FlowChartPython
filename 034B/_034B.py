def Nhap():
    n = int(input("Nhap n: "))
    return n

def Xuli(n):
    s = 0.5
    for i in range(1, n + 1, 2):
        s = s + (2*i + 1) / (2*i + 2)
    return s

def main():
    n = Nhap()
    S = Xuli(n)
    print("Bai 34B")
    print("S(", n, ") = ", S)

if __name__ == "__main__":
    print("Ho Minh Tri")
    main()
