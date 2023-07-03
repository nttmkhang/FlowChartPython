import math

def Nhap():
    x = int (input("Nhap so x: "))
    n = int (input("Nhap so n: "))
    return x, n
        
def TinhTong():
    x, n = Nhap()
    s = 0
    i = 1
    t = 1
    while i <= n:
        t = t * x
        s = math.sqrt(t + s)
        i = i + 1

def main():
   print("Le Thi Bich Loan ")
   print("Bài 097B: ")
   Nhap()
   print("S = ", TinhTong())

if __name__ == "__main__":
    main()
