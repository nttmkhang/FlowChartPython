def Nhap():
    n = int(input('Nhap n : '))
    return n
def TinhTong(n):
    i = 1
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i ** 4)
    return sum
def main():
    n = Nhap()
    print("Ket qua = ",TinhTong(n))
if __name__ == '__main__':
    print('Nguyen Thanh Tai')
    print('Bai 038B')
    main()
