import math

n = int(input("Nhap n: "))
s = 0
t = 1
for i in range(1, n + 1, 1):
    t = t * i
    s = math.pow(s + t, 1/(i + 1))

print("Ho Minh Tri")
print("Bai 100A")
print("S(", n, ") = ", s)
        