import math
print("Tran Thi Mong Truc Ngan")
print("Bai112A")
s = 4 - 2/4 - 1/5 - 1/6
t = 1
e = 1
i = 1
while (e >= math.pow(10,-6)) :
    t = t * 16
    e = (4 / (8 * i + 1 ) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / ( 8 * i + 6)) / t
    s = s + e
    i = i + 1
print("Tong la:", s)



