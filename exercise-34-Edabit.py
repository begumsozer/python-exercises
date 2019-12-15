def who_won(board):
 print(board[0][0])
 x=0
 while x < 3:
  if board[0][x] == board[1][x] and board[0][x] == board[2][x]:
   if board[0][x] == "X" or board[0][x] == "O":
    return(board[0][x])
  if board[x][0] == board[x][1] and board[x][0] == board[x][2]:
   if board[x][0] == "X" or board[x][0] == "O":
    return(board[x][0])
  x=x+1
 if (board[0][0] == board[1][1] and board[0][0] == board[2][2]) or (board[0][2] == board[1][1] and board[0][2] == board[2][0]):
   if board[1][1] == "X" or board[1][1] == "O":
    return(board[1][1])
   
 return("Tie")
 
 print(who_won([
  ["X", "O", "X"],
  ["B", "X", "O"],
  ["X", "B", "B"]]))

print(who_won([['X', 'X', 'O'],
              ['O', 'O', 'X'],
              ['X', 'X', 'O']]))
