print("Nguyen Duy An")
print("Bai 056A: ")
n = int(input("Nhap n : "))
dem = 0
i = 2
while(i<=n):
    if(n%i==0):
        dem=dem+1
    i=i+2
print("So luong uoc so chan : ", dem)