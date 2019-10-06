takım=input("Enter the name of your team in lower case:")
number=input("Enter up to which number of characters you want to split your team's name:")
int_number=int(number)
#convert upper case
buyuk_harf_takım =takım.upper()
print(buyuk_harf_takım)
#split the string
print(buyuk_harf_takım[0:int_number])
uzunluk=(len(buyuk_harf_takım))
print(buyuk_harf_takım[int_number:uzunluk])
