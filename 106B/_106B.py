import math

def Nhap():
    x = int(input("Nhap x: "))
    return x

def Tinh(x):
    xx= (x*3.14)/180
    s = xx
    t = xx
    m=1
    dau = -1
    e = xx
    i = 3
    while (e >= 10**-6):
        t = t * xx * xx
        m = m * (i-1)*i
        e = t/m
        s = s + dau * e
        dau =  - dau
        i = i + 2
    return s

def main():
    print ("Nguyen Duy Vu")
    x = Nhap()
    s = Tinh(x)
    print ('Ket qua:', s)

if __name__ == "__main__":
    main()
