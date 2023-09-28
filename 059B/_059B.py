def Nhap(): 
    n=int(input("Nhap n: ")) 
    return n 
def DemChuSo(n): 
    dem=0 
    t=n 
    while(t!=0): 
        dem=dem+1 
        t=int(t/10) 
    return dem 
def main():
    print("Tên:Nguyễn Tấn Duy")
    print("Bài 059B") 
    n=Nhap() 
    print("Số lượng chữ số của n là: ", DemChuSo(n)) 
if __name__=="__main__": 
    main()

    
