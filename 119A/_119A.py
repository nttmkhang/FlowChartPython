print("Le Duy Nguyen")

n = int(input("Nhap n:"))
aqk = 0
ahh = 0
for i in range(1, n + 1):
    if i == 1:
        aqk = 2
        ahh = 2
    else:
        ahh = (aqk**2 + 2)/(2*aqk)
        aqk = ahh
print("S(n)=", ahh)
