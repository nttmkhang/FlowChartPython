import math

print('Ho Thi Thanh Thao 010A')
x1 = float(input('Nhap x1: '))
y1 = float(input('Nhap y1: '))
x2 = float(input('Nhap x2: '))
y2 = float(input('Nhap y2: '))
x3 = float(input('Nhap x3: '))
y3 = float(input('Nhap y3: '))

a = math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))
b = math.sqrt((x3 - x2)*(x3 - x2) + (y3 - y2)*(y3 - y2))
c = math.sqrt((x3 - x1)*(x3 - x1) + (y3 - y1)*(y3 - y1))

p = a + b + c

print('Chu vi tam giac la: ', p)