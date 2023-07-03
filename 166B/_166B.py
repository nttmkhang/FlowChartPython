def Nhap():
    n=int(input("Nhap n: "))
    return n

def NguyenNhoNhat(n):
    t=1
    k=1
    while 2*t<n:
        t=2*t
        k+=1
    return k

def main():
    n=Nhap()
    print('So nguyen k nho nhat de 2^k > n la:',NguyenNhoNhat(n))

if __name__=="__main__":
    print('Ho Thi Bich Phuong')
    print('Bai 166:')
    main()
