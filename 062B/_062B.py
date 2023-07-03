def Nhap():
    n=int(input("Nhap n: "))
    return n

def TongChan(n):
    s=0
    t=n
    while t!=0:
        dv=t%10
        if dv%2==0:
            s=s+dv
        t=int(t/10)
    return s

def main():
    print("To Hoang Huy")
    n=Nhap()
    print("Tong cac chu so chan cua",n,"la:",TongChan(n))

if __name__ == "__main__":
    main()
