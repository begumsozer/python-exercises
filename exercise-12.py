#Get a number and print from 1 to that number on the same line

a = 1
number=input("Enter a number:")
b=int(number)
while a<=b:
    print(a, end="  ")
    a += 1
