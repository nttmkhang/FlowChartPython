print('Nguyen Vu Binh')
print('Bai 148B')
def Nhap():
    n = int(input())
    return n

def ktToanChan(n):
    flag = 1
    t = n
    while t != 0:
        dv = t % 10
        if dv % 2 != 0:
            flag = 0
        t = t // 10
    return flag

def Xuat(n, flag):
    if flag == 1:
        print(n, 'toan chan')
    else:
        print(n, 'khong toan chan')

def main():
    print('Nhap n: ')
    n = Nhap()
    flag = ktToanChan(n)
    Xuat(n, flag)

if __name__ == "__main__":
    main()