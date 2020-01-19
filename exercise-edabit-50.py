def word_game(p1, p2):
 word=[]
 x=0
 while x < len(p1):
   if p1[x] in word:
    return("Player 2 wins!")
   word.append(p1[x])
   if p1[x][-1] != p2[x][0]:
     return("Player 1 wins!")
   if p2[x] in word:
    return("Player 1 wins!")
   word.append(p2[x])
   if x+1 == len(p1):
    return("Game Continues...")
   if p2[x][-1] != p1[x+1][0]:
     return("Player 2 wins!")
   x=x+1
 return("Game Continues...")

print(word_game(["edabit", "yellow", "growing"], ["tangy", "wedding", "round"]))
print(word_game(["edabit", "yellow", "growing", "dart", "tangy"], ["tangy", "wedding", "ground", "toast", "yellow"]))
print(word_game(["edabit", "yellow", "growing"], ["tangy", "wedding", "ground"]))
