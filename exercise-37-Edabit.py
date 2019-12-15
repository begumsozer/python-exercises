def letter_number(input_string):
  conversion={"a":"4",
              "e":"3",
              "i":"1",
              "o":"0",
              "s":"5"}
  output_string=""
  input_string=input_string.lower()
  for x in input_string:
    if x in conversion:
     output_string=output_string+conversion[x]
    else:
      output_string=output_string+x
  return(output_string)

print(letter_number("Ae42iOsb6R"))
