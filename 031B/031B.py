def Nhap():
	n = int(input('Nhap n: '))
	return n

def Tong(n):
    s = 0
    i = 1
    while i <= (2 * n + 1):
        s = s + 1 / i
        i = i + 2
    return s

def main():
   print("Le Thi Bich Loan ")
   print("Bài 031B: ")
   n = Nhap()
   print("S = ", Tong(n))
    
if __name__ == "__main__":
    main()
