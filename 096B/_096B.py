import math

def nhap():
    print("Nguyen Duc Thanh Duy 21520774")
    n = int(input("Nhap so n: "))
    return n

def xuat(s):
    print("Tong s la: ", s)


def tingTong(n):
    s = 0
    t = 1
    i = 1

    while(i <= n):
        t *= i
        s = math.sqrt(t + s)
        i += 1

    return s


def main():
    n = nhap()
    s = tingTong(n)
    xuat(s)


if __name__ == "__main__":
    main()