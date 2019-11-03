def sayı_bulma(random_number,tahmin):
  if tahmin > random_number:
    return("buyuk")
  elif tahmin < random_number:
    return("kucuk")
  else:
    return("esit")

import random
random_number=random.randint(1,20)

tahmin_sayisi=1
sonuc=""
while sonuc != "esit":
  print("Enter your guess between 1-20:")
  tahmin=int(input())
  sonuc=sayı_bulma(random_number,tahmin)
  if sonuc == "kucuk":
   print("Your guess is smaller")
  elif sonuc == "buyuk":
   print("Your guess is higher")
  else:
   txt="Congratulations!!! You found at {0} guesses"
   print(txt.format(tahmin_sayisi))
  tahmin_sayisi=tahmin_sayisi+1 
