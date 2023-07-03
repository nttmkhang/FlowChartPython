print('Tran Nguyen Chi Huy')
def TichUocSo(n):
    t = 1
    for i in range(1, n + 1):
        if n % i == 0:
            t = t * i
    return t

def main():
    n = int(input("Nhap n: "))
    print("Tich cac uoc so: ", TichUocSo(n))

if __name__ == "__main__":
    main()