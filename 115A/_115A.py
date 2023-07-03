print("Le Huu Do")

n = int(input("Nhap n: "))
att = -1
at = 3
ahh = 3
i = 2
while i <= n:
    ahh = 5 * at + 6 * att
    i += 1
    att = at
    at = ahh
print("a(n) = ", ahh)
