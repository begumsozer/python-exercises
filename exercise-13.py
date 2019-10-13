#nested loop exrcise

number=input("Enter a number:")
int_number=int(number)
print(int_number)
y=1
while y <= int_number:
 m=1
 while m <= int_number:
   z=y*m
   txt="{0} * {1} = {2}"
   print(txt.format(y,m,z))
   m=m+1
 y = y+1
