print("Cao Van Hoang")
n = int(input("Nhap n: "))
lc = n % 10
dem = 0
t = n
while t != 0:
    dv = t % 10
    if dv < lc:
        lc = dv
    t //= 10
t = n
while t != 0:
    dv = t % 10
    if dv == lc:
        dem+=1
    t //= 10
print("So chu so nho nhat cua n la: ",dem)
