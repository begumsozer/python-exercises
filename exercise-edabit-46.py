def collatz(n):
 counter=1
 max_number=n
 while n!=1:
  if n%2 == 0:
   n=(n/2)
  else:
   n=(3*n)+1
  counter += 1
  if n > max_number:
   max_number=n
 return(counter,max_number)

print(collatz(3))
