equals=0
 counter=1
 pin_len=len(pin)
 
 if pin_len != 4 and pin_len != 6:
  return(False)

 if pin.isdigit()==False:
  return(False)

 while counter <= pin_len-1:
  if pin[counter-1] == pin[counter]:
   equals=equals+1
  counter=counter+1
 
 if equals == 3 and pin_len == 4:
  return(False)
 elif equals == 5 and pin_len == 6:
	 return(False)

 return(True)
