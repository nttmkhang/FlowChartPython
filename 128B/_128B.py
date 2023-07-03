def Nhap():
    a = float(input("Nhap a:"))
    b = float(input("Nhap b:"))
    return a,b

def DoiCho(a,b):
    if(a>b):
        a,b = b,a
    return a,b

def main():
    print("To Hoang Huy")
    a,b = Nhap()
    a,b = DoiCho(a,b)
    
    print("a va b theo thu tu tang dan: ",a,b)
    

if __name__ == "__main__":
    main()
