print("Trần Minh Chính: ")
print("Bài 079: ")

n = int(input("Nhap n: "))
s = 0
t = 1
i = 1

while (i <= n):
    t = t * i
    s = s + i * t
    i = i + 1

print("S =", s)