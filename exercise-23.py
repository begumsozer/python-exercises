def print_menu():
  print("  ------Menu-------   ")
  print("1-List current stocks")
  print("2-Update the stocks")
  print("3-List current prices")
  print("4-Update current prices")
  print("5-Customer purchase")
  print("6-Quit menu")
  text_sayi=input()
  while True:
    if text_sayi.isdigit():
     sayi=int(text_sayi)
     if sayi >=1 and sayi <=6:
       return(sayi)
     else:
       text_sayi=input() 
    else:
      text_sayi=input()



    
def print_stocks(fruit_stocks):
 print("Current Stocks: ")
 for x in fruit_stock:
  txt="  {0}:{1} kg"
  print(txt.format(x,fruit_stock[x]))

def print_prices(fruit_price):
 print("Current Prices:")
 for x in fruit_price:
  txt="  {0}:{1} $"
  print(txt.format(x,fruit_price[x]))

def price_calculator(f_customer,f_stock,f_price,fruit,kilos,counter):
 price_counter=0
 total_price=0
 while price_counter<counter:
  if fruit_stock[fruit[price_counter]]>=kilos[price_counter]:
   total_price=(f_price[fruit[price_counter]]* kilos[price_counter]) + total_price 
   
   fruit_stock[fruit[price_counter]]=fruit_stock[fruit[price_counter]]-kilos[price_counter]
   
   fruit_customer[fruit[price_counter]]=fruit_customer[fruit[price_counter]]+kilos[price_counter]
  else:
   total_price=(f_price[fruit[price_counter]]* fruit_stock[fruit[price_counter]]) + total_price
   
   fruit_customer[fruit[price_counter]]=fruit_customer[fruit[price_counter]]+fruit_stock[fruit[price_counter]]
   
   fruit_stock[fruit[price_counter]]= 0
   
  price_counter=price_counter+1 

 return(total_price)

def customer_purchase():  
 fruit=[]
 counter=0
 kilos=[]  
  
 while True:
  print("enter the fruit:")
  fruit.append(input())
  if fruit[counter] in fruit_stock:
    print("how much kg:")
    kilos.append(int(input()))
  else:
    break
  counter=counter+1

 total_price=price_calculator(fruit_customer,fruit_stock,fruit_price,fruit,kilos,counter)
 print("you bought")
 for x in fruit_customer:
  txt="  {0}:{1}"
  print(txt.format(x,fruit_customer[x]))

 txt="you have to pay:{0}$"
 print(txt.format(total_price))
 print("---------------------")
 
fruit_stock={
  "apple":100,
  "banana":120,
  "orange":90,
  "strawberry":70,
  "mango":55
}

fruit_price={
  "apple":3,
  "banana":5,
  "orange":2,
  "strawberry":4,
  "mango":5
}

fruit=[]
counter=0
kilos=[]

menu_item=0
while menu_item != 6:
 menu_item=print_menu()
 if menu_item == 1:
  print_stocks(fruit_stock)
 elif menu_item == 3:
   print_prices(fruit_price)
 elif menu_item == 5:
  fruit_customer={
  "apple":0,
  "banana":0,
  "orange":0,
  "strawberry":0,
  "mango":0
  } 
  customer_purchase() 
 
exit()

print("current stocks: ")
print_stocks(fruit_stock)
print("current prices:")
print_prices(fruit_price)

while True:
  print("enter the fruit:")
  fruit.append(input())
  if fruit[counter] in fruit_stock:
    print("how much kg:")
    kilos.append(int(input()))
  else:
    break
  counter=counter+1

total_price=price_calculator(fruit_customer,fruit_stock,fruit_price,fruit,kilos,counter)
print("you bought")
for x in fruit_customer:
  txt="  {0}:{1}"
  print(txt.format(x,fruit_customer[x]))

txt="you have to pay:{0}$"
print(txt.format(total_price))
print("---------------------")
print("updated stocks:")
print_stocks(fruit_stock)
