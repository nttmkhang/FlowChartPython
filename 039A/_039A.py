print('Nguyen Thanh Tai')
print('Bai 039A')
n = int(input("Nhap n: "))
s = 0
for i in range(1, n + 1):
    s = s + i * (i + 1)
print("S(",n,") = ", s)
