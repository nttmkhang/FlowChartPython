def Nhap():
    n=float(input("Nhap n:   "))
    return n
def KtNamNhuan(n):
    if(n%4==0 and n%100!=0 or n % 400 == 0):
        print("La nam nhuan")
    else:
        print("Khong la nam nhuan")

def main():
    print("Nguyen Xuan Quang")
    print("Bai 135B")
    n = Nhap()
    KtNamNhuan(n)
if __name__ == "__main__":
    main()

