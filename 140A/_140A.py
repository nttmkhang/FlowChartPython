print("___Tran Huynh Nha Uyen___")
print("___Bai 140A____")

import math
a = int(input("Nhap a: "))
b = int(input("Nhap b: ")) 
c = int(input("Nhap c: "))
delta = b*b - 4*a*c 
if (delta < 0):
    print("Phuong trinh vo nghiem ")
if (delta == 0):
    x =-b/2*a
    print("Phuong trinh co 1 nghiem la ", x)
if (delta > 0):
    x1 = (-b + math.sqrt(delta)) / 2*a
    x2 = (-b - math.sqrt(delta)) / 2*a
    print ("Phuong trinh co 2 nghiem la ", x1 , " va ", x2)

