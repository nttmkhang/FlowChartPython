print("Ngo Huong Giang")

def Nhap():
    n = int(input("Nhap n: "))
    return n

def LietKeUocLe(n):
    i = 1
    while i <= n:
        if n % i == 0:
            print(i)
        i += 1

def main():
    n = Nhap()
    print("Cac uoc so le cua n la: ")
    LietKeUocLe(n)

if __name__ == "__main__":
    main()