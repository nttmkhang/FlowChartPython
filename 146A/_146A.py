print("Le Duy Nguyen")

n = int(input("Nhap n: "))
dn = 0
t = n
while t != 0:
    dv = t % 10
    dn = dn * 10 + dv
    t = t//10
if dn == n:
    print("n la so doi xung")
else:
    print("n khong la so doi xung")
