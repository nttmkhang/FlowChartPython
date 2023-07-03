import math

print("Nguyen Duc Thanh Duy 21520774")
n = int(input("Nhap so n: "))
s = 0
t = 1
i = 1

while(i <= n):
    t *= i
    s = math.sqrt(t + s)
    i += 1

print("Tong s la: ", s)