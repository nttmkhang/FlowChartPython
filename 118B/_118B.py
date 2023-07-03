print("Le Huu Do")

def Nhap():
    n = int(input("Nhap n: "))
    return n

def a(n):
    at = 2
    ahh = 2
    i = 2
    while i <= n:
        ahh = (-9 * at - 24) / (5 * at + 13)
        i += 1
        at = ahh
    return ahh

def main():
    n = Nhap()
    print("a(n) = ", a(n))

if __name__ == "__main__":
    main()