print("Pham Hoang Duy")
print("Bai 065")
n = int(input("Nhap n: "))
lc = n % 10
t = n
while t!=0:
    dv = t % 10
    if dv < lc:
        lc = dv
    t //= 10
print("Chu so nho nhat cua so",n,"la:",lc)

