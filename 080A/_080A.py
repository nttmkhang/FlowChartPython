print ('Vo Xuan Thao')
print('Bai 080A: ')

x = eval(input('Nhap x:'))
n = eval(input('Nhap n:'))
s = 1
t = 1
i = 1
while(i<=n):
    t = t * x
    s = s + (i + 1 ) * t
    i = i + 1
print('S = ', s)
