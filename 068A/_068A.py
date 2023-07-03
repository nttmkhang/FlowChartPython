
print('Nguyen Trong Ninh Bai 068A')
n = int(input("Nhap n : "))
s = 0
t = 1
i = 1
while(i<=n):
    t = t * i
    s = s + t
    t = t / 10
print( "s: ", s)
