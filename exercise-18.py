
#finds car rental cost
def kiralama_ucreti(x,y):
 if x>7:
  return ((x*y)-50)
 elif x>=4 and x<=7:
  return ((x*y)-20)
 else:
  return (x*y)

#finds hotel cost
def otel_ucret(gun_sayisi,gecelik_ucret):
  return(gun_sayisi*gecelik_ucret)

#finds airplane cost
def ucak_ucret(sehir):
  if sehir=="Athens":
   return(100)
  elif sehir=="Berlin":
    return(150)
  elif sehir=="London":
    return(200)
  else:
    return(250)
  
#finds total cost  
def toplam_ucret(gun_sayisi,araba_gunluk_ucret,otel_gecelik_ucret,sehir):
 arac_kiralama_tutari=kiralama_ucreti(gun_sayisi,araba_gunluk_ucret)
 otel_tutari=otel_ucret(gun_sayisi,otel_gecelik_ucret)
 ucak_tutari=ucak_ucret(sehir)
 toplam_tutar=arac_kiralama_tutari+otel_tutari+ucak_tutari
 return(toplam_tutar)

print("Enter number of cities you will visit: ")
sehir_sayisi=int(input())
toplam_seyahat=0
sehir_artis=1
while sehir_sayisi > 0:
 txt="Enter name of city  {0}:"
 print(txt.format(sehir_artis))
 sehir=input()
 print("How many days you will stay:")
 x=int(input())
 print("Enter daily car rental rate:")
 y=int(input())
 print("Enter daily hotel rate:")
 gecelik_ucret=int(input())
 
 print("--------")
 txt="Airplane cost: {0}"
 print(txt.format(ucak_ucret(sehir)))
 txt="Car rental cost: {0}"
 print(txt.format(kiralama_ucreti(x,y)))
 txt="Hotel cost: {0}"
 print(txt.format(otel_ucret(x,gecelik_ucret)))
 sehir_basi_ucret=toplam_ucret(x,y,gecelik_ucret,sehir)
 txt="Total cost of staying in {0}: {1}"
 print(txt.format(sehir,sehir_basi_ucret))
 toplam_seyahat=toplam_seyahat + sehir_basi_ucret
 sehir_sayisi=sehir_sayisi-1
 sehir_artis=sehir_artis+1 
 print("--------")

print("*****************************")
txt="Total cost of the trip: {0}"
print(txt.format(toplam_seyahat))
