def Nhap():
    n = int(input("Nhap n: "))
    return n

def Tinh(n):
    s = float(1)
    i = int(1)

    while i<=n:
        s = 1/(1+s)
        i+=1
    return s

def main():
    n = Nhap()
    print("22521519")
    print("Bai 164B")
    print("S(n)= ", Tinh(n))

if __name__ == "__main__":
    main()