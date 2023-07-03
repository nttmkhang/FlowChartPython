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
    return flag

def main():
    print("Le Thi Bich Loan ")
    print("Bài 162B: ")
    n = Nhap()
    if ktGiamDan(n)==1 :
        print("Giam")
    else:
        print("Khong giam")

if __name__ == "__main__":
    main()

