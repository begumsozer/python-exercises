def min_turns(current, target):
  total=0
  for x in range (len(current)):
    int_current=int(current[x])
    int_target=int(target[x])
    if int_current <= int_target:
      forward=int_target-int_current
      backward=int_current+(10-int_target)
    elif int_target<int_current:
      forward(10-int_current)+int_target
      backward=int_current-int_target
    total+=min(forward,backward)
  return total
