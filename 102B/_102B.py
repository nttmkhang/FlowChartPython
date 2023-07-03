import math
def Tong():
    s = 0
    e = 0.5
    i = 2
    while e >= math.pow(10,-6):
        e = 1 / i
        s = s + e
        i += 2
    return s
def main():
    print("Nguyễn Thị Tuyết Loan - 22520783 - Bài 102")
    print("Tong:", Tong())
if __name__ == "__main__":
    main()
