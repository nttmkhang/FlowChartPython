def Nhap():
    n = int(input("Nhap n: "))
    return n

def ktTonTaiSoChan(n):
    flag = False
    t = n
    while(t!=0):
        dv = t % 10
        if(dv%2 == 0):
            flag = True
        t = t // 10
    if (flag == True):
        print(n,"ton tai chu so chan")
    else: 
        print(n,"khong ton tai chu so chan")

def main():
    print("Bai 066B")
    n = Nhap()
    ktTonTaiSoChan(n)

if __name__ == "__main__":
    print("Nguyen Huynh Duy Hieu")
    main()