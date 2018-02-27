aks=int(input("Enter the number:"))
temp=aks
rev=0
while(aks>0):
    dig=aks%10
    rev=rev*10+dig
    aks=aks//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")