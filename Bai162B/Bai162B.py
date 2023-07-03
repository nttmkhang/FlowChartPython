def Nhap():
    n=int(input("Nhap n: "))
    return n
def ktGiamDan(n):
    flag=1
    t=n
    while t>=10:
        dv=t%10
        hc=int(t/10)%10
        if hc<dv:
            flag=0
        t=int(t/10)
    if flag==1 :
        print("Giam")
    else:
        print("Khong giam")

def main():
    print("Bai 162B: 21521083")
    n = Nhap()
    ktGiamDan(n)
if __name__ == "__main__":
    main()

