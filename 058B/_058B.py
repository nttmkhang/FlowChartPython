def Nhap():
    n=int(input("Nhập n: ")) 
    return n 
def Tong_chu_so(n): 
    tong=0 
    t=n 
    while(t!=0): 
        dv=t%10 
        tong=tong+dv 
        t=int(t/10) 
    return tong 
def main(): 
    print("Tên:  Đặng Lê Bình")
    print("Bài 058B") 
    n=Nhap() 
    print("Tổng các chữ số của số nguyên dương n là ",Tong_chu_so(n))
if __name__=="__main__": 
    main()