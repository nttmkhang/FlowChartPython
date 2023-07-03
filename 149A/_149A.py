print('Nguyen Vu Binh')
print('Bai 149A')
a = int(input('Nhap a: '))
b = int(input('Nhap b: '))
m = abs(a)
n = abs(b)
while m * n != 0:
    if m > n:
        m = m - n
    else:
        n = n - m
ucln = m + n
print('UCLN: ', ucln)