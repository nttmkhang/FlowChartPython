
if __name__ == "__main__":
    print("Nguyen Hoang Hy - 21520946")
    n = int(input("Nhap n: "))
    s = 0

    for i in range(1, n + 1):
        s += 1 / i

    print("Ket qua la: ", s)