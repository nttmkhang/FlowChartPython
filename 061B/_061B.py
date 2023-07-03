def Nhap():
    n = int(input("Nhap n: "))
    return n

def DemSoLe(n):
    dem = 0
    t = n
    while (t != 0):
        dv = t % 10
        if (dv % 2 != 0):
            dem = dem + 1
        t = int(t/10)
    return dem
    
def main():
    print("Bui Thai Hoang")
    n = Nhap()
    kq = DemSoLe(n)
    print("So luong chu so le la: ",kq)
    
if __name__ == "__main__":
    main()
