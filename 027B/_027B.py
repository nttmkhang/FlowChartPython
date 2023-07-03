
def Nhap():
    n = int(input("Nhap n: "))
    return n

def TinhTong(n):
    s = 0
    i = 1
    while i <= n:
        s = s + i
        i += 1
    return s

def main():
    print("21520963 - Nguyen Tuan Khang Bai 027B: ")
    n = Nhap()
    print('S = ', TinhTong(n))

if __name__ == "__main__":
    main()