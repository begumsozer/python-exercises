#exercise 11.1

letter=input("Enter a letter:")
print(letter)

number=input("Enrer a number:")
int_number=int(number)
print(int_number)

i=1
while i <= int_number:
 print(i*letter[0])
 i =i+1

#exercise 11.2

#Gets a number and prints the multiplication table from 1 to the number entered.

number=input("enter a number:")
int_number=int(number)
print(int_number)
 
y=1
while y <= int_number:
 x=y*int_number
 txt="{0} * {1} = {2}"
 print(txt.format(y,int_number,x))
 y =y+1

#exercise 11.3

#Get a number. Add 1 to the number. Subtract 2 from the number and print the result until number is equal or less than 1

number=input("Enter a number:")
i=int(number)
i= i + 1
while i > 2:
 i-=2
 print(i)
