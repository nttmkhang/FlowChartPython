
def main():
     print('Phan Trọng Tính')
     print('Bai 032A')
     n = int (input("Nhap so n: "))
     s = 0
     i = 1
     while i <= n:
        s = s + 1 / i*(i+1)
        i = i + 1
     print('Tong la: ', s)
     
if __name__ == "__main__":
    main()
