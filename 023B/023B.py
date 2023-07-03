def Nhap():
    n = int(input('Nhap n: '))
    return n

def HangChuc(n):
    hc = int((n/10) % 10)
    return hc

def main():
    print('Vu Hoang')
    print('Bai 023A')
    
    n = Nhap()
    hc = HangChuc(n)
    print('Hang chuc la:', hc)

if __name__ == "__main__":
	main()
