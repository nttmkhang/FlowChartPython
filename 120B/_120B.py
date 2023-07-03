import math

print("Le Duy Nguyen")

def Nhap() :
    n = int(input("Nhap n:"))
    return n

def SoHangThu(n) :
    at = 2
    i = 2
    while i <= n:
        ahh = 5 * at + math.sqrt(24 * (at ** 2) - 8)
        i = i + 1   
        at = ahh
    return ahh

def main() :
    n = Nhap()
    S = SoHangThu(n)
    print("So hang thu",n,"cua day so la:",S)

if __name__ == "__main__" :
    main()
