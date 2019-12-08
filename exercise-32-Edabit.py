def is_mini_sudoku(square):
 count=[0,0,0,0,0,0,0,0,0]
 for x in square:
   for y in x:
     if y < 1 or y > 9:
       return(False)
     if count[y-1] == 1:
       return(False)
     else:
       count[y-1]=1
 return(True)
