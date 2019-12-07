def find_formul(input_string):
 symbol_list=["*","/","+","-"]
 symbol=" "
 for x in symbol_list:
   if input_string.find(x) > 0:
     symbol=x
     break
 if symbol == " ":
    return(int(input_string))
 
 splited_input=input_string.split(symbol)
 number_1=int(splited_input[0])
 number_2=int(splited_input[1])
 if symbol == "*":
   return(number_1*number_2)
 elif symbol == "/":
   return(number_1/number_2)
 elif symbol == "+":
   return(number_1+number_2)
 elif symbol == "-":
   return(number_1-number_2)
 
print("enter math expression:")
input_string=input()

result=find_formul(input_string)
print(result)
