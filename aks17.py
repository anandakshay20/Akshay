m=int(input("Enter the number: "))
a=list(map(int,str(m)))
b=list(map(lambda x:x**3,a))
if(sum(b)==m):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. "