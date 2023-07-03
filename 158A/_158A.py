print("To Hoang Huy")
n = int(input("Nhap n: "))
lc = n%10
dem = 0
t = n
while t != 0:
    dv = t % 10
    if dv > lc:
        lc = dv
    t = int(t/10)
t = n
while t != 0:
    dv = t % 10
    if dv == lc:
        dem +=1
    t = int(t/10)
print("So chu so lon nhat cua n la: ",dem)


