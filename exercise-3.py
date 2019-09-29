text_sayı=input("enter an integer: ")
tam_sayı_1=int(text_sayı)
ondalık_sayı_1=float(tam_sayı_1)
txt="integer is converted to float as: {0}"
print(txt.format(ondalık_sayı_1))

text_sayı=input("enter a float number: ")
ondalık_sayı_2=float(text_sayı)
tam_sayı_2=int(ondalık_sayı_2)
txt="float converted to integer is: {0}"
print(txt.format(tam_sayı_2))

sayı1=tam_sayı_1*tam_sayı_2
txt="multiply of integers: {0}"
print(txt.format(sayı1))

sayı2=ondalık_sayı_1*ondalık_sayı_2
txt="multiply of float numbers: {0}"
print(txt.format(sayı2))

toplam=sayı1+sayı2
txt="sum of multiply of integers and multiply of floats: {0}"
print(txt.format(toplam))
