
print('Tran Nguyen Chi Huy')
def ToanLe(n):
   flag = 1
   t = n
   while t != 0:
        dv = t % 10
        if dv % 2 == 0:
            flag = 0
        t = t // 10
   return flag

def main():
    n = int(input("Nhap n: "))
    flag = ToanLe(n)
    if flag == 1:
        print("Toan le")
    else:
        print("Khong toan le")

if __name__ == "__main__":
    main()


