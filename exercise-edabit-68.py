def magic_square_game(alice, bob):
  a=alice[0]-1
  b=bob[0]-1
  list_a=list(alice[1])[b]
  list_b=list(bob[1])[a]
  if list_a == list_b:
    return True
  else:
    return False
