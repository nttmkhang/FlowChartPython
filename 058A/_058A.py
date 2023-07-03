print("Tên: Đặng Lê Bình") 
print("Bài 058A") 
n=int(input("Nhập n: ")) 
tong=0 
t=n 
while(t!=0): 
    dv=t%10 
    tong=tong+dv 
    t=int(t/10) 
print("Tổng các chử số của số nguyên dương n là ", tong)
