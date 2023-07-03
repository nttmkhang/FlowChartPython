print("Cao Van Hoang")
n = int(input("Nhap n: "))
tich = 1
t = n 
while t != 0:
    dv = t % 10
    if dv % 2 != 0:
        tich *= dv
    t = int(t / 10)
print("Tich cac chu so le cua n la:",tich)