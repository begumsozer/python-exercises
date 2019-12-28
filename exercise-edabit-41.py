def bill_split(spicy,cost):
 friend=0
 me=0
 for x in range(0,len(spicy)):
   if spicy[x]=="S":
    me+=cost[x]
   elif spicy[x]=="N":
     me+=cost[x]/2
     friend+=cost[x]/2
 output=[me,friend]    
 return(output)

spicy=["N","N","S"]
cost=[10,10,5]
print(bill_split(spicy,cost))
