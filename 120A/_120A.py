import math

print("Le Duy Nguyen")

n = int(input("Nhap n: "))
at = 2
i = 2
while i <= n:
    ahh = 5 * at + math.sqrt(24 * (at ** 2) - 8)
    i = i + 1   
    at = ahh
print("ahh = ", ahh)
