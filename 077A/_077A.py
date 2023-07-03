print("Mai Dinh Khoi")
print('Bai 077A')

k = float(input("Nhap k: "))
n = int(input("Nhap n: "))

s = 0
i = 1
while( i <= n):
    s = s + pow(i, k)
    i = i + 1

print("s=", s)
