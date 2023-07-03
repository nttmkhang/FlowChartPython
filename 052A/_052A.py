print("Le Huu Do")

n = int(input("Nhap n: "))
dem = 0
i = 1
while i <= n:
    if n % i == 0:
        dem += 1
    i += 1
print("So luong uoc so cua n la: ", dem)
