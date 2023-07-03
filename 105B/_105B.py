import math
def TinhToan():
    s=0
    m=0
    e=1
    i=1
    while(e > math.pow(10, -6)):
        m = m + i
        e = 1/m
        s = s + e
        i = i + 1
    return s

def main():
    print("Tran Nhat Tan")
    kq=TinhToan()
    print("\nS(n) = ",round(kq,6),".\n")

if __name__=="__main__":
    main()

