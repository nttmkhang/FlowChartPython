def Nhap():
    x = float(input('Nhap x: '))
    n = int(input('Nhap n: '))
    return x, n

def TinhTong(x, n):
    s = 0
    t = 1
    m = 0
    i = 1
    dau = -1
    while i <= n:
        t = t * x
        m = m + i
        s = s + dau * t / m
        i = i + 1
        dau = -dau
    return s

def main():
    print('Vu Hoang')
    print('Bai 023A')
    
    x, n = Nhap()
    s = TinhTong(x, n)
    print('S(x, n) =', s)

if __name__ == "__main__":
	main()
