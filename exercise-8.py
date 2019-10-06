number=input("Enter first number: ")
int_number=int(number)

number_2=input("Enter second number: ")
int_number_2=int(number_2)

number_3=input("Enter third number: ")
int_number_3=int(number_3)

list=[int_number,int_number_2,int_number_3]
list.sort(reverse=False)
txt="Numbers sorted from small to large: {0}"
print(txt.format(list))
list.sort(reverse=True)
txt="Numbers sorted from large to small: {0}"
print(txt.format(list))
