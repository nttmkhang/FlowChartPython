import math
print("Pham Hoang Duy")
print("Bai 131")
def Nhap():
    xA = float(input("Nhap xA: "))
    yA = float(input("Nhap yA: "))
    xB = float(input("Nhap xB: "))
    yB = float(input("Nhap yB: "))
    xC = float(input("Nhap xC: "))
    yC = float(input("Nhap yC: "))
    return xA,yA,xB,yB,xC,yC
def KiemTra(xA,yA,xB,yB,xC,yC):
    a = math.sqrt((xB-xA)**2+(yB-yA)**2)
    b = math.sqrt((xC-xB)**2+(yC-yB)**2)
    c = math.sqrt((xA-xC)**2+(yA-yC)**2)
    if a + b > c and a + c > b and b + c > a:
        return 1
    return 0
def Xuat(xA,yA,xB,yB,xC,yC):
    if KiemTra(xA,yA,xB,yB,xC,yC) == 1:
        print("ABC la tam giac!")
    else: 
        print("ABC la khong la tam giac!")
def main():
    xA,yA,xB,yB,xC,yC = Nhap()
    Xuat(xA,yA,xB,yB,xC,yC)
if __name__ == "__main__":
    main()



