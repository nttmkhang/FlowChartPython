def Nhap():
    n = int(input("Nhap n: "))
    return n

def ktTonTaiLe(n):
    flag = 0 
    t = n 
    while t != 0: 
        dv = t % 10 
        if dv % 2 != 0: 
            flag = 1 
        t = t // 10
    return flag

def main():
    n = Nhap()
    if ktTonTaiLe(n) == 1: 
        print("Ton tai so le") 
    else: 
        print("Khong ton tai so le")

if __name__ == "__main__":
    print("Tran Tuan Vu")
    main()

