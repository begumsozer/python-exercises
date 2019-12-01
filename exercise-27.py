sayi=1
while sayi <= 10:
  print(sayi)
  sayi=sayi+1

for x in range(1,11):
  print(x)

sayilar=[]
for x in range (0,10):
  sayilar.append((x+1)*2)

#for x in sayilar:
  #print(sayilar[x])

x=0
while x < 10:
  print(sayilar[x])
  x=x+1

for x in range(0,10):
  print(sayilar[x])

for x in sayilar:
  print(x)

ad_soyad="begum_sozer"

for x in ad_soyad:
  print(x)

sayac=0
while sayac < len(ad_soyad):
  print(ad_soyad[sayac])
  sayac=sayac+1

for x in range (1,100):
  txt="{0}----{1}"
  print(txt.format(x,100-x))

print("sayi giriniz:")
sayi=int(input())
for y in range(1,sayi+1):
  print("*"*y)
for y in range(sayi,0,-1):
  print("*"*y)

print("a:")
a=int(input())
print("b:")
b=int(input())
print("c:")
c=int(input())
for y in range(a,b):
  if y % c == 0:
    print(y)

for x in range(1,16):
  if x%2==0:
    print(x)

toplam=0
for x in range(0,11):
  if x % 2 == 0:
    toplam=toplam+x
print(toplam)
