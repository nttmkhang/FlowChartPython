<<<<<<< HEAD
﻿def Nhap():
    n = int(input("Nhap n: "))
    return n
def KiemTra(n):
    flag = 1
    t = n
    while t >= 10:
        dv = t % 10
        hc = (t/10) % 10
        if hc < dv:
            flag = 0
        t = t / 10
    return flag
def main():
    n = Nhap()
    flag = KiemTra(n)
    print("Nguyễn Thị Tuyết Loan - 22520783 - Bài 162")
    if flag == 1:
        print("Giam")
    else:
        print("Khong giam")
if __name__ == "__main__":
    main()
=======
def Nhap():
    n = int(input("Nhap n: "))
    return n
def ktGiamDan(n):
    flag = 1
    t = n
    while t>=10:
        dv = t % 10
        hc = int(t / 10) % 10
        if hc < dv:
            flag = 0
        t = int(t / 10)
    return flag

def main():
    print("Bai 162")
    n = Nhap()
    if(ktGiamDan(n)):
        print(n,"la so nguyen giam dan")
    else: 
        print(n,"khong phai la so nguyen giam dan")

if __name__ == "__main__":
    main()

>>>>>>> d6149d2ad5d5cae8946bcb3daced3b2faa3f4e2a
