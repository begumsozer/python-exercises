def print_square(height,length,letter):
  print(length*letter)
  for x in range(0,height-2):
    print(letter+((length-2)*" ")+letter)
  print(length*letter)
  return()

print_square(7,10,"/")
