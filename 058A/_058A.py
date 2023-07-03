print("Ten: Dang Le Binh") 
print("Bai 058A") 
n=int(input("Nhap n: ")) 
tong=0 
t=n 
while(t!=0): 
    dv=t%10 
    tong=tong+dv 
    t=int(t/10) 
print("Tong cac chu so cua so nguyen n la ", tong)
