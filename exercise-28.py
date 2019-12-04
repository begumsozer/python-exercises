import random

def print_matrix(matrix):
  for x in matrix:
    for y in x:
     print(y,end="  ")
    print("\n") 
  return

def generate_random():
  row=random.randrange(1,5)
  colon=random.randrange(1,5)
  return(row,colon)

def take_input(user_input):
  while True:
   print(user_input)
   input_number=input()
   if input_number.isdigit():
    int_input_number=int(input_number)
    if int_input_number>=1 and int_input_number <=5:
      return(int_input_number)
    else:
      print("Enter between 1 and 5")
   else:
    print("Enter a numeric value")
 
def control(row,user_row,colon,user_colon):
 if row == user_row and colon == user_colon:
   return(True)
 else:
   return(False)

  
matrix= [["o","o","o","o","o"],
         ["o","o","o","o","o"],
         ["o","o","o","o","o"],
         ["o","o","o","o","o"],
         ["o","o","o","o","o"]
        ]
        
row,colon=generate_random()
txt="{0} {1}"
print(txt.format(row,colon))
counter=0
while counter < 5:
 print_matrix(matrix)
 user_row=take_input("row:")
 user_colon=take_input("colon:")
 if control(row,user_row,colon,user_colon) == True:
  print("You won")
  matrix[row-1][colon-1]="+"
  print_matrix(matrix)
  break
 else:
  counter=counter+1
  txt="trial {0} is wrong"
  print(txt.format(counter))
  matrix[user_row-1][user_colon-1]="x"


if counter > 4:
 print("You lost")
 matrix[row-1][colon-1]="+"
 print_matrix(matrix)
