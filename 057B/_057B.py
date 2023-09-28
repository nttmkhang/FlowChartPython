


def Nhap():
    n=int(input("Nhap n:  "))
    return n 
def Tong_uoc_so(n): 
    i=1 
    s=0 
    while(i<n): 
        if(n%i==0): 
            s=s+i 
        i=i+1 
    return s 
def main():
    print("Tên: Đặng Lê Bình") 
    print("Bài 057B") 
    n=Nhap() 
    print("Tổng các ước số nhỏ hơn n là ", Tong_uoc_so(n)) 
if __name__=="__main__": 
    main()