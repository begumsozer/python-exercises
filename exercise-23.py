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

def get_stock_and_prices(file_name):
 market_file=open(file_name,"r")
 for x in market_file:
  splited_line=x.split(" ")
  fruit=splited_line[0]
  stock=splited_line[1]
  price=splited_line[2]
  fruit_stock[fruit] = int(stock)
  fruit_price[fruit]= int(price[0:-1])
 market_file.close()

def write_stock_and_prices(file_name):
 market_file=open(file_name,"w")
 for x in fruit_stock:
   stock_file=x+" "+str(fruit_stock[x])+" "+str(fruit_price[x])+"\n"
   market_file.write(stock_file)

def update_price():
  print("Enter fruit name:")
  fruit_name=input()
  print("Enter new price:")
  new_price=int(input())
  fruit_price[fruit_name]=new_price

def update_stock():
  print("Enter fruit name:")
  fruit_name=input()
  print("Enter new stock:")
  new_stock=int(input())
  fruit_stock[fruit_name]=new_stock


fruit_stock={}
fruit_price={}

fruit=[]
counter=0
kilos=[]

get_stock_and_prices("market.txt")

menu_item=0
while menu_item != 6:
 menu_item=print_menu()
 if menu_item == 1:
  print_stocks(fruit_stock)
 elif menu_item == 2:
   update_stock()
 elif menu_item == 3:
   print_prices(fruit_price)
 elif menu_item == 4:
   update_price()
 elif menu_item == 5:
  fruit_customer={} 
  for x in fruit_stock:
    fruit_customer[x]=0
  customer_purchase() 

write_stock_and_prices("market_2.txt")

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
