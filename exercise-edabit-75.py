def over_twenty_one(cards):
  tot=0
  face='JQK'
  for card in cards:
    if str(card) in face:
      tot+=10
    elif card=='A':
        tot+=1
    else:
      tot+=card
  if tot <= 21:
    return False
  else:
    return True
