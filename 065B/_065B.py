print("Pham Hoang Duy")
print("Bai 065")

def Nhap():
    n = int(input("Nhap n: "))
    return n
def NhoNhat(n):
    lc = n % 10
    t = n
    while t!=0:
        dv = t % 10
        if dv < lc:
            lc = dv
        t //= 10
    return lc
def main():
    n = Nhap()
    print("Chu so nho nhat cua so",n,"la:",NhoNhat(n))
if __name__ == "__main__":
    main()

