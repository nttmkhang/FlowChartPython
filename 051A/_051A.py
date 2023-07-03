
print('Tran Nguyen Chi Huy')
n = int(input("Nhap n: "))
t = 1
for i in range(1, n + 1):
    if n % i == 0:
        t = t * i
print("Tich cac uoc so: ", t)