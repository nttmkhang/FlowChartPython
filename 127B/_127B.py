def Nhap():
   a = int(input("Nhap a: "))
   b = int(input("Nhap b: "))
   return a, b

def GiaTriNhoNhat(a, b):
    lc = a
    if(lc > b):
        lc = b
    return lc
    
def main():
    print("Bui Thai Hoang")
    a, b = Nhap()
    kq = GiaTriNhoNhat(a, b)
    print("Gia tri nho nhat: ",kq)

if __name__ == "__main__":
    main()