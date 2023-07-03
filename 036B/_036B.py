
def Nhap():
    n = int(input("Nhap n: "))
    x = int(input("Nhap x: "))
    return n, x
def LuyThua(n, x):
    t = 1
    i = 1
    while i <= n:
        t *= x
        i += 1
    return t
def main():
    print("Nguyễn Thị Tuyết Loan - 22520783 - Bài 036")
    n, x = Nhap()
    print("Luy thua" , x, "cua", n, " :", LuyThua(n, x))
if __name__ == "__main__":
    main()

