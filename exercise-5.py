number=input("Enter a number: ")
int_number=int(number)
b=100
c=1000
if int_number < b:
 print("The number you entered is < 100 ")
elif int_number >= b and int_number < c:
  print("The number you entered is >=100 and <1000 ")
else:
  print("The number you entered is >= 1000")
