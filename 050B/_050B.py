print("Ngo Huong Giang")

def Nhap():
    n = int(input("Nhap n: "))
    return n

def TongUocSo(n):
    s = 0
    i = 1
    while i <= n:
        if n % i == 0:
            s = s + i
        i = i + 1
    return s

def main():
    n = Nhap()
    print("Tong cac uoc so cua ", n, "la: ", TongUocSo(n))

if __name__ == "__main__":
    main()