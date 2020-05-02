def sum_of_holes(N):
  dict={0:1, 4: 1, 6:1, 8:2, 9:1}
  counter=0
  for x in range(1,N+1):
    for num in str(x):
      n=int(num)
      if n<10 and n in dict:
        counter+=dict[n]
  return counter
