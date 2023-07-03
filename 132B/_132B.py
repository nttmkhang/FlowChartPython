def Nhap():
    x = float(input("Nhap x: "))
    y = float(input("Nhap y: "))
    return x,y
def DienTichTamGiac(xA, yA, xB, yB, xC ,yC):
    dientich = abs(xA*yB + xB*yC + xC*yA - xB*yA - xC*yB - xA*yC)/2
    return dientich
def ktThuocTamGiac(xA, yA, xB, yB, xC ,yC, xM ,yM):
    ABC = DienTichTamGiac(xA, yA, xB, yB, xC ,yC)
    MAB = DienTichTamGiac(xA, yA, xB, yB,xM ,yM)
    MBC = DienTichTamGiac(xB, yB, xC ,yC, xM ,yM)
    MAC = DienTichTamGiac(xA, yA, xC ,yC, xM ,yM)
    S = MAB + MBC + MAC
    if S == ABC:
        return 1
    else:
        return 0
def main():
    print("Bai 132B")
    print("Nhap toa do dinh A: ")
    xA,yA = Nhap()
    print("Nhap toa do dinh B: ")
    xB,yB = Nhap()
    print("Nhap toa do dinh C: ")
    xC,yC = Nhap()
    print("Nhap toa diem M: ")
    xM,yM = Nhap()
    kq = ktThuocTamGiac(xA, yA, xB, yB, xC ,yC, xM ,yM)
    if kq == 1:
        print("Diem M thuoc tam giac ABC")
    else:
        print("Diem M khong thuoc tam giac ABC")
if __name__ == "__main__":
    print("Nguyen Huynh Duy Hieu")
    main()
