def nhap():
    print("Nguyen Duc Thanh Duy 21520774")
    n = int(input("Nhap so n: "))
    return n

def xuat(s):
    print("Tong s la: ", s)
   

def tinhTong(n):
    
    s = 0
    i = 1

    while(i <= n):
        s += i * i
        i += 1

    return s

def main():
    n = nhap()
    s = tinhTong(n)
    xuat(s)


if __name__ == "__main__":
    main()
   
    