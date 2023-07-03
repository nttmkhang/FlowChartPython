print('Vu Hoang')
print('Bai 023A')

x = float(input('Nhap x: '))
n = int(input('Nhap n: '))
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
print('S(x, n) =', s)
