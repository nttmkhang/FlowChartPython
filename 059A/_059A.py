print("Tên: Nguyễn Tấn Duy") 
print("Bài 59A")
n=int(input("Nhap n: ")) 
dem=0 
t=n 
while(t!=0): 
    dem=dem+1 
    t=int(t/10) 
print("Số lượng chữ số của n là", dem)
