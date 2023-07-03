print("Tên: Đặng Lê Bình")
print("Bài 057A")
n=int(input("Nhập n: ")) 
i=1 
s=0 
while(i<n): 
    if(n%i==0):
        s=s+i 
    i=i+1 

print("Tổng các ước số của n và nhỏ hơn n là", s)
