print('Tran Nguyen Chi Huy')
n = int(input("Nhap n: "))
s = 0
for i in range(2, n + 1, 2):
    if n % i == 0:
        s = s + i
print("Tich cac uoc so: ", s)
