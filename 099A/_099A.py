import math
n = int(input("Nhap n: "))

s = int(0)
i = int(1)

while i<=n:
    s = pow(i+s, 1/(i+1))
    i+=1

print("22521519")
print("Bai 099A")
print("S(n)=", s)
