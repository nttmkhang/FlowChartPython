print("Le Huu Do")

def Nhap():
    n = int(input("Nhap n: "))
    return n
def a(n):
    att = -1
    at = 3
    ahh = 3
    i = 2
    while i <= n:
        ahh = 5 * at + 6 * att
        i += 1
        att = at
        at = ahh
    return ahh

def main():
    n = Nhap()
    print("a(n) = ", a(n))

if __name__ == "__main__":
    main()
