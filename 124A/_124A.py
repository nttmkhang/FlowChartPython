print("Tran Quang Anh Kiet")
n = int(input("Nhap n: "))
at = 2
bt = 1
ahh = 0
bhh = 0
for i in range (2,n+1):
    ahh = at*at + 2*bt*bt
    bhh = 2*bt*at
    at = ahh
    bt = bhh
print("a(",n,")= ", ahh, sep='')
print("b(",n,")= ",bhh , sep ='')


