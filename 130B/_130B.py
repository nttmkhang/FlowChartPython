print('Doan Quang Huy')
print('Bai 130')
def Nhap():
    x = int(input('Nhap x: '))
    y = int(input('Nhap y: '))
    z = int(input('Nhap z: '))
    return x,y,z
def ktTamGiac(x,y,z):
    if ((x+y>z)and(x+z>y)and(y+z>x)):
        return 1
    else: return 0
def main():
    x,y,z=Nhap()
    if ktTamGiac(x,y,z):
        print('La tam giac')
    else: print ('Khong la tam giac')
if __name__ == "__main__":
    main()


