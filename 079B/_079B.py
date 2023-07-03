def Nhap():
    n = int(input("Nhap n: "))
    return n

def Tinh(n):
    s = 0
    t = 1
    i = 1
    while (i <= n):
        t = t * i
        s = s + i * t
        i = i + 1
    return s

def main():
    n = Nhap()
    print("S =", Tinh(n))

if __name__ == "__main__":
    print("Trần Minh Chính")
    print("Bài 079: ")
    main()
