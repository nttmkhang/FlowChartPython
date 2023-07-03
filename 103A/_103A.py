print("Tran Nhat Tan")

s=0
e=1
i=1
while e>=10**-6:
    e=1/i
    s+=e
    i+=2

print("\nS(n) = ",round(s,6),".\n")