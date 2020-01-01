def profit(info):
 total_sales=info["sell_price"]*info["inventory"]
 total_cost=info["cost_price"]*info["inventory"]
 result=round((total_sales-total_cost))
 return result
 
result=profit({"cost_price":32.67,
        "sell_price":45.00,
        "inventory":1200})


print(result)
