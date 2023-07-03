
print("___Tran Huynh Nha Uyen___")
print("___Bai 110A____")

n = float(input("Nhap n: "))
s = 0
dau=1
e = 4
i = 1 
while(e>=10**-6):
    e = 4/i
    s +=dau*e
    i+=2
    dau=-dau
   
print ("S(n) = ", s)