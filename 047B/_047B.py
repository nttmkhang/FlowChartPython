import math as m

def Nhap():
    n = int(input("Nhap n: "))
    return n

def S(n):
    s = 0
    for i in range(1, n + 1):
        s = s + m.sqrt(1 + 1 / i ** 2 + 1 / (i + 1) ** 2)
    return s

def main():
    print("Tran Tue Tanh")
    print("Bai 047B")
    n = Nhap()
    print("S(n): ", S(n))

if __name__ == "__main__":
    main()