print("Le Duy Nguyen")

def Nhap() :
    n = int(input("Nhap n:"))
    return n

def SoHangThu(n) :
    aqk = 0
    ahh = 0
    for i in range(1, n + 1):
        if i == 1:
            aqk = 2
            ahh = 2
        else:
            ahh = (aqk**2 + 2)/(2*aqk)
            aqk = ahh
    return ahh

def main() :
    n = Nhap()
    S = SoHangThu(n)
    print("So hang thu",n,"cua day so la:",S)

if __name__ == "__main__" :
    main()
