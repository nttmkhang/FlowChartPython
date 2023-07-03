def Nhap():
    n = int(input("Nhap n: "))
    return n

def TinhPi(n):
    s = 0
    dau=1
    e = 4
    i = 1 
    while(e>=10**-6):
        e = 4/i
        s +=dau*e
        i+=2
        dau=-dau
    return s

def main():
    print("___Tran Huynh Nha Uyen___")
    print("___Bai 110B____")
    n=Nhap()
    print("pi= ", TinhPi(n))


if __name__=="__main__":
    main()
