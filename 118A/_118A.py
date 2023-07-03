print("Le Huu Do")

n = int(input("Nhap n: "))
at = 2
ahh = 2
i = 2
while i <= n:
    ahh = (-9 * at - 24) / (5 * at + 13)
    i += 1
    at = ahh
print("a(n) = ", ahh)