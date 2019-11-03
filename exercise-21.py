def sayı_bulma(random_number,tahmin):
  dogru_tahmin=0
  yanlis_tahmin=0
  sayi=0
  while sayi < 3:
   if tahmin [sayi] == random_number[sayi]:
    dogru_tahmin=dogru_tahmin+1
   else:
    yanlis_tahmin=yanlis_tahmin+1
   sayi=sayi+1
  return(dogru_tahmin,yanlis_tahmin)

import random
random_number=random.randint(100,999)
random_string=str(random_number)
#print(random_string)
tahmin_sayisi=1
sonuc=""
while True:
  print("Enter your guess:")
  tahmin=input()
  dogru_tahmin,yanlis_tahmin=sayı_bulma(random_string,tahmin)
  if dogru_tahmin == 3:
   txt="Congratulations !!! You found at {0} guesses :))"
   print(txt.format(tahmin_sayisi))
   break
  else:
    txt="Correct number of digits:{0}. Incorrect number of digits:{1} :(("
    print(txt.format(dogru_tahmin,yanlis_tahmin))
  tahmin_sayisi=tahmin_sayisi+1 
