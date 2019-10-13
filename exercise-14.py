#exercise 14.1

number=input("Enter a number:")
int_number=int(number)
i = 1
print("Dividends of the number you entered: ")
while i <= int_number : 
 if (int_number % i==0) : 
  print (i) 
 i = i + 1

#exercise 14.2

number=input("Enter a number: ")
int_number=int(number)
n=int_number
y=0
while n >= 1:
 y = y + n
 n = n - 1
txt="Sum of the numbers from 1 to {0}: {1}"
print(txt.format(int_number,y))

#exercise 14.3

number=input("Enter a number: ")
int_number=int(number)
n=int_number
y=1
while n >= 1:
 y = y * n
 n = n - 1
txt="Factorial of {0}: {1}"
print(txt.format(int_number,y))
