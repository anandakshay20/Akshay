def power(aks,hike):
    if(hike==1):
        return(aks)
    if(hike!=1):
        return(aks*power(aks,hike-1))
aks=int(input("Enter aks: "))
hike=int(input("Enter hike value: "))
print("Result:",power(aks,hike))