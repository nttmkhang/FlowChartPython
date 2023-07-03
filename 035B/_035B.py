def Nhap():
    n=int(input("Nhap n: "))
    return n

def GiaiThua(n):
    t=1
    for i in range(1,n+1):
        t=t*i
    return t

def main():
    n=Nhap()
    print('T(',n,') = ',GiaiThua(n))

if __name__=="__main__":
    print('Ho Thi Bich Phuong')
    print('Bai 035:')
    main()
