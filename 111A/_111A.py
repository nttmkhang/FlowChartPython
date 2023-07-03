import math
print("Bai 111A ")
print("Ho Kim Thien Nga")
pi = 3
dau = 1
e = 3
i = 1
while (e >= math.pow(10, (-6))):
    e = 4 / ( 2 * i * ( 2 * i + 1 ) * ( 2 * i + 2 ))
    pi += dau*e
    dau = - dau
    i += 1
print("pi = ", pi)
