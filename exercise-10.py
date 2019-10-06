name=input("Enter your name and surname: ")
letter=input("Enter a letter:")
length=len(name)

if name[0] == letter[0] and name[-1] == letter[0]:
 first_letter= letter[0]
 first_letter_upper = first_letter.upper()
 last_letter=letter[-1]
 last_letter_upper=last_letter.upper()
 print(first_letter_upper+name[1:length-1]+last_letter_upper)
elif name[0] == letter[0]:
 first_letter= letter[0]
 first_letter_upper = first_letter.upper()
 print (first_letter_upper+name[1:length])
elif name[-1] == letter[0]:
 last_letter=letter[-1]
 last_letter_upper=last_letter.upper()
 print (name[0:length-1]+last_letter_upper)
else:
 name_upper=name.upper()
 print(name_upper)
