import math
print("Pham Hoang Duy")
print("Bai 131")
xA = float(input("Nhap xa: "))
yA = float(input("Nhap ya: "))
xB = float(input("Nhap xb: "))
yB = float(input("Nhap yb: "))
xC = float(input("Nhap xc: "))
yC = float(input("Nhap yc: "))
a = math.sqrt((xB-xA)**2+(yB-yA)**2)
b = math.sqrt((xC-xB)**2+(yC-yB)**2)
c = math.sqrt((xA-xC)**2+(yA-yC)**2)
if a + b > c and a + c > b and b + c > a:
    print("ABC la tam giac!")
else:
    print("ABC khong la tam giac!")

