

print('Nguyen Trong Ninh')
print('Bai 068')
n = int(input("Nhap n : "))
s = 0
t = 1
i = 1
while(i<=n):
    t = t * i
    s = s + t
    t = t / 10
print( "s: ", s)
