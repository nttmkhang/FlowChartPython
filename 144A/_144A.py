print("Phan Nguyen Khoa - Bai 144A")
n = int(input("Nhap n: "))
dem = 0
for i in range(1, n + 1, 1):
    if n % i == 0:
        dem += 1
if dem == 2:
    print(n, "la so nguyen to")
else:
    print(n, "khong la so nguyen to")
