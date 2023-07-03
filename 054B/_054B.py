
print('Tran Nguyen Chi Huy')
def TongUocSoChan(n):
    s = 0
    for i in range(2, n + 1, 2):
        if n % i == 0:
            s = s + i
    return s

def main():
    n = int(input("Nhap n: "))
    print("Tong cac uoc so chan: ", TongUocSoChan(n))

if __name__ == "__main__":
    main()
