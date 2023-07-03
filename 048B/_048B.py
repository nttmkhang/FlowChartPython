def Nhap():
   x= float(input("Nhap x:"))
   n= int(input("Nhap n: "))
   return x,n
def Tong(x,n):
    s= 1
    for i in range(1,n+1,1):
        s = s * (x + i -1) * ( x + i )
        print("S(x,n)=",s)
        return s
def main():
    print("Phan Nguyen Khoa - Bai 048B")
    x,n = Nhap()
    s = Tong(x,n)
if __name__ == "__main__":
    main()

