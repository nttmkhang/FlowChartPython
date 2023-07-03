def SoHangThun(n):
    at = 2
    bt = 1
    ahh = 0
    bhh = 0
    for i in range (2,n+1):
        ahh = 3*bt+2*at
        bhh = at+ 3*bt
        at = ahh
        bt = bhh
    print("a(",n,")= ", ahh, sep='')
    print("b(",n,")= ",bhh , sep ='')

def main():
    print("Tran Quang Anh Kiet")
    n = int(input("Nhap n: "))
    SoHangThun(n)

if __name__ == "__main__":
    main()

