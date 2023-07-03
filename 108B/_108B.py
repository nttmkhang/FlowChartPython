import math
def Nhap():
    x = int(input("Nhap x: "))
    return x

def Tinh(x):
    s = 1
    t = 1
    m = 1
    e = 1
    i = 1
    while (e >= 10**-6):
        t = t * x
        m = m * i
        e = t/m
        s = s + e
        i = i + 1
    return s

def main():
    print ("Nguyen Duy Vu")
    x = Nhap()
    s = Tinh(x)
    print ('Ket qua:', s)

if __name__ == "__main__":
    main()
