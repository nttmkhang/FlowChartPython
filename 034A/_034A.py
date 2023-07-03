n = int(input("Nhap n: "))
s = 0.5
for i in range(1, n + 1, 2):
    s = s + (2*i + 1) / (2*i + 2)

print("Ho Minh Tri")
print("Bai 34A")
print("S(", n, ") = ", s)