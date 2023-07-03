print("Nguyen Huynh Duy Hieu")
print("Bai 066A")
n = int(input("Nhap n: "))
flag = False
t = n
while(t!=0):
    dv = t % 10
    if(dv%2 == 0):
        flag = True
    t = t // 10
if(flag == True):
    print(n,"ton tai chu so chan")
else: 
    print(n,"khong ton tai chu so chan")