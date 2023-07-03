import math
print ('Nguyen Duy Vu')
x = int(input("Nhap x: "))
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
print (s)

