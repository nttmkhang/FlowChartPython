print('Huynh Gia Bao')
print('Bai 109A')

s = 1
m = 1
e = 1
i = 1
while (e >= 10**(-6)):
    m *= i
    e = 1/m
    s += e
    i += 1
print('e = ', s)
