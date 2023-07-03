
print('Tran Nguyen Chi Huy')
def SoHangDay(n):
    att = -1
    at = 3
    t = 2
    for i in range(2, n + 1):
        t = t * 2
        ahh = 5 * t + 5 * at - att
        att = at
        at = ahh
    return ahh

def main():
    n = int(input("Nhap n: "))
    print("ahh: ", SoHangDay(n))

if __name__ == "__main__":
    main()