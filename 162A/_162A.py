print("Nguyen Huynh Duy Hieu")
print("Bai 162A")
n = int(input("Nhap n: "))
flag = True
t = n
while (t>=10):
    dv = t % 10
    hc = int(t / 10) % 10
    if(hc < dv):
        flag = False
    t = int(t / 10)
if (flag == True):
    print(n,"la so nguyen giam dan")
else: 
    print(n,"khong phai la so nguyen giam dan")
