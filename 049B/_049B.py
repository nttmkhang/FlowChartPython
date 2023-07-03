print("Le Huu Do")

def Nhap():
    n = int(input("Nhap n: "))
    return n

def LietKeUoc(n):
    i = 1
    while i <= n:
        if n % i == 0:
            print(i)
        i += 1

def main():
    n = Nhap()
    print("Cac uoc so cua n la: ")
    LietKeUoc(n)

if __name__ == "__main__":
    main()