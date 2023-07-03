print("Nguyễn Phước Hưng")
print("Bài 071")

x = eval(input("Nhap x: "))
n =eval(input("Nhap n: "))
s = x
t = x
i = 3
while(i < 2 * n + 1):
    t = t * x * x
    s = s + t
    i = i + 2
print("s = ", s)

