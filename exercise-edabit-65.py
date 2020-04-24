def seq_level(lst):
 def level(lst,level_cnt):
   set_lst=set(lst)
   length = len(set_lst)
   if length == 1: 
     return level_cnt
   new_lst=[]
   counter=1
   while counter < length:
    difference=lst[counter]-lst[counter-1]
    new_lst.append(difference)
    counter+=1
   return level(new_lst,level_cnt+1)
 level_cnt=level(lst,0)
 if level_cnt == 1:
  return "Linear"
 elif level_cnt == 2:
  return "Quadratic"
 else:
  return "Cubic"
