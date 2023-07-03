def Nhap():
    n = int(input("Nhap n: "))
    return n

def KiemTra(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s = s + i
    if s == n:
        return True
    else:
        return False

def main():
    print("Tran Tue Tanh")
    print("Bai 143B")
    n = Nhap()
    if KiemTra(n):
        print(n, "la so hoan thien")
    else:
        print(n, "khong la so hoan thien")

if __name__ == "__main__":
    main()