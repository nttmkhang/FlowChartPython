print("Nguyen Tan Duy")
n=int(input("Nhap n: "))
tich=1
t=n
while t!=0:
dv=t%10
tich=tich*dv
t=int(t/10)
print("Tich cac chu so cua",n,"la: ",tich)
