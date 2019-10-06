number=input("Enter first number: ")
int_number=int(number)
number_2=input("Enter second number:")
int_number_2=int(number_2)
total=int_number + int_number_2
if total < 20 and total > 15 :
 print("Sum of two numbers you entered are between 15 and 20")
 print(total)
else:
 print("Sum of two numbers you entered are not between 15 and 20") 
 print(total)
 print("Multiply of two numbers you entered: ") 
 print(int_number*int_number_2)
