
def Nhap():
    n = int(input("Nhap n: "))
    return n

def Tinh(n):
    s = 0

    for i in range(1, n + 1):
        s += 1 / i

    return s



def main():
    print("Nguyen Hoang Hy - 21520946")
    n = Nhap()

    print("Ket qua la: ", Tinh(n))

if __name__ == "__main__":
    main()