def TinhToan():
    s=0
    e=0.5
    i=1
    while e>=10**-6:
        e=1/(i*(i+1))
        s+=e
        i+=1
    return s

def main():
    print("Tran Nhat Tan")
    kq=TinhToan()
    print("\nS(n) = ",round(kq,6),".\n")

if __name__=="__main__":
    main()
