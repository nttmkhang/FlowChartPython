print("Le Huu Do")

def Nhap():
    n = int(input("Nhap n: "))
    return n

def DemUoc(n):
    i = 1
    dem = 0
    while i <= n:
        if n % i == 0:
            dem += 1
        i += 1
    return dem

def main():
    n = Nhap()
    print("So luong uoc so nguyen duong cua n la: ", DemUoc(n))

if __name__ == "__main__":
    main()
