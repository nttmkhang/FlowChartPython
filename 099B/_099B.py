import math

def Nhap():
    n = int(input("Nhap n: "))
    return n

def Tinh(n):
    s=int(0)
    i=int(1)
    while i<=n:
        s = pow(i+s, 1/(i+1))
        i+=1
    return s

def main():
    n = Nhap()
    print("22521519")
    print("Bai 099B")
    print("S(n)= ", Tinh(n))

if __name__ == "__main__":
    main()


        