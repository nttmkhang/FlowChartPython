
def main():
    print("Bai 031A: 21521083")
    n = int(input('Nhap n: '))
    s = 0
    i = 1
    while i <= (2 * n + 1):
        s = s + 1 / i
        i = i + 2
    print("S = ", s)
    
if __name__ == "__main__":
    main()