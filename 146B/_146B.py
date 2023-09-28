print("Le Duy Nguyen")

def Nhap() :
    n = int(input("Nhap n: "))
    return n

def KiemTraDoiXung(n) :
    dn = 0
    t = n
    while t != 0:
        dv = t % 10
        dn = dn * 10 + dv
        t = t//10
    if dn == n:
        return 1
    return 0

def main() :
    n = Nhap()
    if KiemTraDoiXung(n) == 1 :
        print("n la so doi xung")
    else :
        print("n khong la so doi xung")

if __name__ == "__main__" :
    main()
