import random
random_1=random.randrange(1,6)
random_2=random.randrange(1,6)
print(random_1,random_2)
total=random_1+random_2
print(total)
if total == 7 or total == 11: 
 print("you won :))")
elif total == 2 or total == 3 or total == 12:
 print ("you lost :((")
else :
 print("drawn !!") 
