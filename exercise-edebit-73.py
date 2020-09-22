def reorder_digits(lst, direction):
  new_lst=[]
  for x in lst:
    number="".join(sorted(str(x)))
    if direction=="asc":
      new_lst.append(int(number))
    else:
      new_lst.append(int(number[::-1]))
  return new_lst
