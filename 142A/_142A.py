print("Tran Thi Mong Truc Ngan")
print("Bai142A")
n = int(input("Nhap n: "))
dn = 0
t = n
while (t != 0):
    dv = t % 10
    dn = dn * 10 + dv
    t = t // 10
print("So dao nguoc cua ", n ," la: ", dn)


