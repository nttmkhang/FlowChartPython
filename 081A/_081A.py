print('Tran Ngoc Nhat Vy')
print('Bai 081A')

x = float(input('Nhap x: '))
n = int(input('Nhap n: '))
s = 0
i = 0
m = 1
while i <= n:
    m = m * (x + i)
    s = s + float(1 / m)
    i = i + 1
print('S(',x,',',n,") = ", s)