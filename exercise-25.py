fruit_stock={}
fruit_price={}

market_file=open("market.txt","r")

for x in market_file:
  splited_line=x.split(" ")
  fruit=splited_line[0]
  stock=splited_line[1]
  price=splited_line[2]
  fruit_stock[fruit] = stock
  fruit_price[fruit]=price 
market_file.close()
for x in fruit_stock:
  txt="{0} {1} {2} \n"
  print(txt.format(x,fruit_stock[x],fruit_price[x]))
