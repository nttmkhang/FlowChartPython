def Nhap():
    n = int(input("Nhap n: "))
    return n

def TimKLonNhat(n):
    t = 1
    k = 0
    while (2 * t < n):
        t = t * 2
        k = k + 1
    return k

def main():
    n = Nhap()
    k = TimKLonNhat(k)
    print("Bai 165B")
    print("So nguyen k lon nhat de 2^k < n la: ", k)

if __name__ == "__main__":
    print("Ho Minh Tri")
    main()
