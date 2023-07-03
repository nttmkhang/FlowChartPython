def Nhap():
    n = int(input("Nhap n: "))
    return n

def TinhTong(n):
    s = 0
    for i in range(n):
        s = s + (i+1)*(i+2)*(i+3)
    return s

def main():
    print("___Tran Huynh Nha Uyen___")
    print("___Bai 044B____")
    n=Nhap()
    print("S(n): ", TinhTong(n))


if __name__=="__main__":
    main()