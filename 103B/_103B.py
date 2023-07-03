def TinhToan():
    s=0
    e=1
    i=1
    while e>=10**-6:
        e=1/i
        s+=e
        i+=2
    return s

def main():
    print("Tran Nhat Tan")
    kq=TinhToan()
    print("\nS(n) = ",round(kq,6),".\n")

if __name__=="__main__":
    main()

