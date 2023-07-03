def Nhap():
    n = int(input("Nhap n: "))
    return n

def Tinh(n):
    at = 1
    bt = 1
    for i in range (2, n + 1):
        ahh = 3 * bt + 2 * at
        bhh = at + 3 * bt
        at = ahh
        bt = bhh
    return ahh, bhh

def main():
    print("Tang Thanh Thien")
    n = Nhap()
    print("(ahh, bhh) =", Tinh(n))

if __name__ == "__main__":
    main()
