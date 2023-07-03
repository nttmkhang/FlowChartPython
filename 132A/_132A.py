print("Nguyen Huynh Duy Hieu")
print("Bai 132A")
print("Nhap toa do dinh A: ")
xA = float(input("Nhap xA: "))
yA = float(input("Nhap yA: "))
print("Nhap toa do dinh B: ")
xB = float(input("Nhap xB: "))
yB = float(input("Nhap yB: "))
print("Nhap toa do dinh C: ")
xC = float(input("Nhap xC: "))
yC = float(input("Nhap yC: "))
print("Nhap toa diem M: ")
xM = float(input("Nhap xM: "))
yM = float(input("Nhap yM: "))
SABC = abs(xA*yB + xB*yC + xC*yA - xB*yA - xC*yB - xA*yC) / 2
SMAB = abs(xA*yB + xB*yM + xM*yA - xB*yA - xM*yB - xA*yM) / 2
SMAC = abs(xA*yM + xM*yC + xC*yA - xM*yA - xC*yM - xA*yC) / 2
SMBC = abs(xM*yB + xB*yC + xC*yM - xB*yM - xC*yB - xM*yC) / 2
S = SMAB + SMBC + SMAC
if (S == SABC):
    print("M nam trong tam giac ABC")
else: 
    print("M nam ngoai tam giac ABC")





