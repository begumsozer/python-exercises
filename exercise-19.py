def hesaplama_v1(a,b):
 cevre=2*(a+b)
 alan=a*b
 return(cevre,alan)

def hesaplama_v2(a,b):
 sonuc=[0,0]
 cevre=2*(a+b)
 alan=a*b
 sonuc[0]=cevre
 sonuc[1]=alan
 return(sonuc)

print("Input side a of the rectangle:")
a_kenar=int(input())
print("Input side b of the rectangle:")
b_kenar=int(input())

cevre,alan=hesaplama_v1(a_kenar,b_kenar)
print(cevre,alan)

sonuc=hesaplama_v2(a_kenar,b_kenar)
print(sonuc[0],sonuc[1])
