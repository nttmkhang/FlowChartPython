import math

def main():
    print("Bai 097A: 21521083")
    x = int (input("Nhap so x: "))
    n = int (input("Nhap so n: "))
    s = 0
    i = 1
    t = 1
    while i <= n:
        t = t * x
        s = math.sqrt(t + s)
        i = i + 1
    print("Tong la: ", s)

if __name__ == "__main__":
    main()