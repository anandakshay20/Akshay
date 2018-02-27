aks=int(input("Enter the number: "))
s=0
for i in range(2,aks//2+1):
    if(aks%i==0):
        s=s+1
if(s<=0):
    print("Number is prime")
else:
    print("Number isn't prime")