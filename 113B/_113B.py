def Nhap():
    n = int(input("Nhap n: "))
    return n

def Tinh(n):
    at = 2
    for i in range(1, n):
        ahh = at + 2 * i + 1
        at = ahh
    return ahh

def main():
    print("Tran Tue Tanh")
    print("113B")
    n = Nhap()
    print("So hang thu", n, "la: ", Tinh(n))

if __name__ == "__main__":
    main()