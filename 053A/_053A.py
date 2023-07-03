print("Ngo Huong Giang")

n = int(input("Nhap n: "))
print("Cac uoc so le cua n la: ")
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i = i + 1