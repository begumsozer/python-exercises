def ucret(x,y):
 if y<=40:
  return(y*x)
 else:
  return((y-40)*(1.5*x)+(40*x))
 
print("Enter hourly rate:")
x=int(input())
print("Enter hours worked:")
y=int(input())
print("You earned: ", int(ucret(x,y)), "USD")
