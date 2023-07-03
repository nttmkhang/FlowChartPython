print("Ngo Huong Giang")

def Nhap():
    n = int(input("Nhap n: "))
    return n

def Tinh(n):
    att = 1
    at = 2
    i = 2
    while i <= n:
        ahh = 4 * at + att
        i = i + 1
        att = at 
        at = ahh
    return ahh

def main():
    n = Nhap()
    print("So hang thu ", n, "cua day la: ", Tinh(n))

if __name__ == "__main__":
    main()