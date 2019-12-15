def alphabet(number_letter):
  letter_count=0
  letter=" "
  output_string=""
  for x in number_letter:
    if x.isalpha()==True:
      letter=x
    elif x.isdigit()==True:
      letter_count=int(x)
      output_string=output_string+(letter*letter_count)
  return(output_string)

print(alphabet("A4B5C7"))
