
def main():
    print("Bai 162A: 21521083")
    n=int(input("Nhap n: "))
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

if __name__ == "__main__":
    main()


