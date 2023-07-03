def Nhap():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    c = int(input("Nhap c: "))
    return a,b,c

def XuatTangDan(a,b,c):
    if a > b:
        a,b = b,a
    if a > c:
        a,c = c,a
    if b > c:
        b,c = c,b 
    print("Cac so theo thu tu tang dan:",a,b,c)

def main():
    print("Cao Van Hoang")
    a,b,c = Nhap()
    XuatTangDan(a,b,c)

if __name__ == "__main__":
    main()
