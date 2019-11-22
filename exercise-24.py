market_file = open("market.txt", "w")

fruit_stock={
  "apple":100,
  "banana":120,
  "orange":90,
  "strawberry":70,
  "mango":55
}

market_stock={}

for x in fruit_stock:
  txt="{0} {1} \n"
  market_file.write(txt.format(x,fruit_stock[x]))

market_file.close()

market_file=open("market.txt","r")

for x in market_file:
  fruit_counter=x.index(" ")
  fruit=x[0:fruit_counter]
  stock=x[fruit_counter+1:-1]
  market_stock[fruit] = int(stock)*2
  
market_file.close()

for x in market_stock:
  txt="{0} {1} \n"
  print(txt.format(x,market_stock[x]))
