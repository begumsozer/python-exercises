def briscola_score(my_deck1, my_deck2):
  first_round=0
  second_round=0
  points={"3":10,
          "A":11,
          "Q":3,
          "K":4,
          "J":2}
  for x in my_deck1:
    if x[0] in points:
     first_round+=points[x[0]]
  for x in my_deck2:
    if x[0] in points:
      second_round+=points[x[0]]
  first_round=120-first_round
  if second_round > first_round:
    return "You Win!"
  if second_round < first_round:
    return "You Lose!"
  else:
    return "Draw!"
