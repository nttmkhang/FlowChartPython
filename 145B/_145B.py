print('Nguyen Vu Binh')
print('Bai 145B')
def Nhap():
    n = int(input())
    return n

def ktChinhPhuong(n):
    flag = 0
    i = 0
    while i <= n:
        if i * i == n:
            flag = 1
        i = i + 1
    return flag

def Xuat(n, flag):
    if flag == 1:
        print(n, 'la so chinh phuong')
    else:
        print(n, 'khong phai la so chinh phuong')

def main():
    print('Nhap n: ')
    n = Nhap()
    flag = ktChinhPhuong(n)
    Xuat(n, flag)

if __name__ == "__main__":
    main()