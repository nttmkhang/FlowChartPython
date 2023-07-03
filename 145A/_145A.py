print('Nguyen Vu Binh')
print('Bai 145A')
n = int(input('Nhap n: '))
flag = 0
i = 0
while i <= n:
    if i * i == n:
        flag = 1
    i = i + 1
if flag == 1:
    print(n, 'la so chinh phuong')
else:
    print(n, 'khong phai la so chinh phuong')