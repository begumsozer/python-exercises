def day_amount(month, year):
 months={1:31,
          2:28,
          3:31,
          4:30,
          5:31,
          6:30,
          7:31,
          8:31,
          9:30,
          10:31,
          11:30,
          12:31}
 if year % 400 == 0:
   months[2]=29
 elif year % 100 == 0:
   months[2]=28
 elif year % 4 == 0:
    months[2]=29
 return(months[month])

print("month:")
month=int(input())
print("year:")
year=int(input())

print(day_amount(month,year))
