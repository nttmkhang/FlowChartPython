def Nhap():
   n= int(input("Nhap n: "))
   return n
def KiemTra(n):
    for i in range(1, n + 1, 1):
        if n % i == 0:
           dem += 1
    if dem == 2:
        kt=print(n, "la so nguyen to")
    else:
        kt=print(n, "khong la so nguyen to")
    return kt
def main():
    print("Phan Nguyen Khoa - Bai 144B")
    n = Nhap()
    kt=KiemTra(n)
if __name__ == "__main__":
    main()