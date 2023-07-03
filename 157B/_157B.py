def Nhap():
   n = int(input("Nhap n: "))
   return n

def XuatChuoiGiaTri(n):
    s = 0 
    i = 1 
    while(i <= n):
        s = s + float(1/i)
        print(s)
        i = i + 1
    
def main():
    print("Bui Thai Hoang")
    n = Nhap()
    XuatChuoiGiaTri(n)
    
if __name__ == "__main__":
    main()
