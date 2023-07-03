

def main():
     print('Phan Trọng Tính')
     print('Bai 098A')
     n = int (input("Nhap so n: "))
     s = 0
     i = 2
     while i <= n:
         s = (i + s) ** (1 / i)
         i = i + 1
     print('Tong la: ', s)
     
if __name__ == "__main__":
    main()