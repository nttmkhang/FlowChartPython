def Tong():
    s=0
    e=1
    i=1
    while(e>=pow(10,-6)):
        e=1/i
        s+=e
        i+=1
    return s

def main():
    print('Tong S =',Tong())

if __name__=="__main__":
    print('Ho Thi Bich Phuong')
    print('Bai 101:')
    main()