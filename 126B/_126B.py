def Nhap():
    a=int(input("Nhập số a: ")) 
    b=int(input("Nhập số b: ")) 
    return a,b 
def Lon_nhat(a,b): 
    if(a>b):
        return a 
    return b 
def main():
    print("Tên: Đặng Lê Bình") 
    print("Bài 126B") 
    a,b=Nhap()
    print("Số lớn nhất trong hai số là", Lon_nhat(a,b))
if __name__=="__main__":
    main()
