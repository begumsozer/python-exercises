def chosen_wine(wines):
  if len(wines)==0:
    return None
  elif len(wines)==1:
    return wines[0]["name"]
  prices=[]
  for x in wines:
    prices.append(x["price"])
  prices.sort()
  for x in wines:
    if x["price"]==prices[1]:
     return x["name"]
   
print(chosen_wine([
  { "name": "Wine A", "price": 8.99 },
  { "name": "Wine 32", "price": 13.99 },
  { "name": "Wine 9", "price": 10.99 }
]))
