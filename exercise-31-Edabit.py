def can_play(hand, face):
 splited_face=face.split(" ")
 for x in hand:
  splited_hand=x.split(" ")
  if splited_hand[0]==splited_face[0]:
    return(True)
  if splited_hand[1] == splited_face[1]:
    return(True)
 return(False)
