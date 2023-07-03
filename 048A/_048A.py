print ("Phan Nguyen Khoa - Bai 048A")
x = float(input("Nhap x:"))
n = int(input("Nhap n:"))
s = 1
for i in range(1,n+1,1):
    s = s * ( x + i - 1 ) * ( x + i )
print ("S(x,n)=:",s)