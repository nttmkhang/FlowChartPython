print("Tran Nhat Tan")

import math
s = 0
m = 0
e = 1
i = 1
while(e > math.pow(10, -6)):
    m = m + i
    e = 1/m
    s = s + e
    i = i + 1
print("S(n) = ", s)
